import asyncio
import base64
import logging

import cv2
import httpx
import yt_dlp

# 분리된 모듈 import
from src.core.config import settings
from src.core.database import session_local_write
from src.models.video import Video

logger = logging.getLogger("worker.analysis")


class VideoAnalysisService:
    def __init__(self, video_id: int):
        # [수정] db 세션을 인자로 받지 않음 (연결 끊김 방지)
        self.video_id = video_id

    def _get_db(self):
        """DB 세션을 생성하는 헬퍼"""
        return session_local_write()

    def update_status(self, status: str, summary: str = None):
        """DB 세션을 짧게 열고 닫음"""
        db = self._get_db()
        try:
            video = db.query(Video).filter(Video.id == self.video_id).first()
            if video:
                video.analysis_status = status
                if summary:
                    video.ai_summary = summary
                db.commit()
                db.refresh(video)
                logger.info(f"Video {self.video_id} status updated to {status}")
        except Exception as e:
            db.rollback()
            logger.error(f"Failed to update status: {e}")
        finally:
            db.close()  # [중요] 사용 후 즉시 닫음

    def get_stream_url(self, youtube_url: str) -> str:
        # [수정] JS 런타임 오류 방지를 위한 extractor_args 추가
        ydl_opts = {
            "format": "best[ext=mp4]",
            "quiet": True,
            "extractor_args": {
                "youtube": {
                    "player_client": ["android", "web"]  # 모바일 클라이언트 흉내로 JS 우회 시도
                }
            },
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=False)
                return info["url"]
        except Exception as e:
            logger.error(f"yt-dlp failed: {e}")
            return youtube_url

    def extract_keyframes(self, video_url: str, interval_sec: int = 5) -> list:
        frames = []
        try:
            if "youtube.com" in video_url or "youtu.be" in video_url:
                target_url = self.get_stream_url(video_url)
            else:
                target_url = video_url

            cap = cv2.VideoCapture(target_url)
            fps = cap.get(cv2.CAP_PROP_FPS)
            if fps == 0:
                fps = 30  # Fallback
            frame_interval = int(fps * interval_sec)
            count = 0

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                if count % frame_interval == 0:
                    _, buffer = cv2.imencode(".jpg", frame)
                    b64_image = base64.b64encode(buffer).decode("utf-8")
                    frames.append(b64_image)
                    if len(frames) >= 15:
                        break
                count += 1
            cap.release()
            return frames
        except Exception as e:
            logger.error(f"Frame extraction error: {e}")
            raise e

    async def generate_image_description(self, base64_image: str) -> str:
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(
                    f"{settings.OLLAMA_URL}/api/generate",
                    json={
                        "model": "minicpm-v:8b",
                        "prompt": "Describe this image in detail.",
                        "images": [base64_image],
                        "stream": False,
                    },
                )
                if resp.status_code == 200:
                    return resp.json().get("response", "")
                else:
                    logger.error(f"VLM Error: {resp.text}")
                    return "Description failed."
                return ""
        except Exception as e:
            logger.error(f"VLM Connection Error: {e}")
            return ""

    async def summarize_descriptions(self, descriptions: list) -> str:
        if not descriptions:
            return "No descriptions available to summarize."

        full_text = "\n".join([f"Scene {i + 1}: {desc}" for i, desc in enumerate(descriptions)])
        prompt = (
            f"Here are descriptions of scenes from a video:\n{full_text}\n\n"
            "Based on these descriptions, please summarize the overall content of the video in Korean."
        )

        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                resp = await client.post(
                    f"{settings.OLLAMA_URL}/api/generate",
                    json={"model": "exaone3.5:latest", "prompt": prompt, "stream": False},
                )
                if resp.status_code == 200:
                    return resp.json().get("response", "")
                else:
                    return "Summary generation failed."
        except Exception as e:
            logger.error(f"LLM Connection Error: {e}")
            return "Summary generation failed."

    async def generate_thumbnail_prompt(self, summary: str) -> str:
        """Qwen3에게 이미지 생성을 위한 영문 프롬프트 요청"""
        try:
            prompt_instruction = (
                f"Based on the summary below, write a high-quality text-to-image prompt "
                f"for a movie poster style thumbnail. Write ONLY the English prompt.\n\nSummary: {summary}"
            )
            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(
                    f"{settings.OLLAMA_URL}/api/generate",
                    json={
                        "model": "qwen3:latest",
                        "prompt": prompt_instruction,
                        "stream": False,
                        "options": {"temperature": 0.7},
                    },
                )
                return resp.json().get("response", "").strip() if resp.status_code == 200 else ""
        except Exception as e:
            logger.error(f"Prompt gen error: {e}")
            return ""

    async def generate_and_upload_thumbnail(self, summary: str) -> str:
        """이미지 생성 -> 다운로드 -> MinIO 업로드 -> URL 반환"""
        # 1. 프롬프트 생성
        prompt = await self.generate_thumbnail_prompt(summary)
        if not prompt:
            return None

        try:
            # 2. Pollinations.ai로 이미지 생성 요청
            encoded_prompt = urllib.parse.quote(f"cinematic shot, masterpiece, {prompt}")
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1280&height=720&model=flux&seed=42"

            # 3. 이미지 바이너리 다운로드 (메모리)
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.get(image_url)
                if resp.status_code != 200:
                    return None
                image_data = io.BytesIO(resp.content)  # 파일 객체로 변환

            # 4. MinIO 업로드 (Storage Class 활용)
            # 파일명: ai_thumb_{id}_{uuid}.jpg
            filename = f"ai_thumb_{self.video_id}_{uuid.uuid4().hex[:8]}.jpg"
            s3_url = storage_client.upload_file(image_data, object_name=filename)

            return s3_url

        except Exception as e:
            logger.error(f"Thumbnail generation/upload failed: {e}")
            return None

    async def process_video(self):
        # 1. 상태 업데이트 (DB 연결 짧게 사용)
        self.update_status("processing")
        logger.info(f"Starting analysis for Video {self.video_id}")

        url = None
        # 2. URL 조회 (DB 연결 짧게 사용)
        db = self._get_db()
        try:
            video = db.query(Video).filter(Video.id == self.video_id).first()
            if video:
                url = video.url
        finally:
            db.close()

        if not url:
            logger.error("Video URL not found")
            self.update_status("failed")
            return

        # 3. Heavy Task 실행 (DB 연결 없음)
        try:
            # 2. 프레임 추출 (DB 연결 없이 수행)
            logger.info("Extracting frames...")

            frames = await asyncio.to_thread(self.extract_keyframes, url)
            if not frames:
                raise Exception("No frames extracted")

            # 3. Vision Model로 설명 생성 (순차적)
            descriptions = []
            logger.info(f"Analyzing {len(frames)} frames with VLM...")
            for frame in frames:
                desc = await self.generate_image_description(frame)
                if desc:
                    descriptions.append(desc)
            # 4. Text Model로 요약
            logger.info("Summarizing text...")
            summary = await self.summarize_descriptions(descriptions)

            # [NEW] AI 썸네일 생성 및 업로드
            ai_thumb_url = None
            if summary and summary != "Failed":
                ai_thumb_url = await self.generate_and_upload_thumbnail(summary)

            # [NEW] DB 업데이트 (AI 썸네일 플래그 True)
            self.complete_analysis(summary, ai_thumb_url)

        except Exception as e:
            logger.error(f"Processing failed: {e}")
            self.update_status("failed")

    def complete_analysis(self, summary, thumbnail_url):
        db = self._get_db()
        try:
            video = db.query(Video).filter(Video.id == self.video_id).first()
            if video:
                video.analysis_status = "completed"
                video.ai_summary = summary
                if thumbnail_url:
                    video.thumbnail = thumbnail_url
                    video.is_ai_thumbnail = True  # AI 생성 표시
                db.commit()
                logger.info(f"Analysis completed. AI Thumb: {thumbnail_url}")
        finally:
            db.close()
