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
            fps = cap.get(cv2.CAP_PROP_FPS) or 30
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
                logger.error(f"VLM Response Error: {resp.text}")
                return ""
        except Exception as e:
            logger.error(f"VLM Connection Error: {e}")
            return ""

    async def summarize_descriptions(self, descriptions: list) -> str:
        if not descriptions:
            return "No descriptions available to summarize."

        text = "\n".join([f"- {desc}" for desc in descriptions if desc])
        prompt = f"Summarize the video content based on these scene descriptions:\n{text}"

        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                resp = await client.post(
                    f"{settings.OLLAMA_URL}/api/generate",
                    json={"model": "qwen3:latest", "prompt": prompt, "stream": False},
                )
                if resp.status_code == 200:
                    return resp.json().get("response", "")
                return "Summary failed."
        except Exception as e:
            logger.error(f"LLM Error: {e}")
            return "Summary failed."

    async def process_video(self):
        # 1. 상태 업데이트 (DB 연결 짧게 사용)
        self.update_status("processing")

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
            frames = await asyncio.to_thread(self.extract_keyframes, url)

            descriptions = []
            for frame in frames:
                desc = await self.generate_image_description(frame)
                if desc:
                    descriptions.append(desc)

            summary = await self.summarize_descriptions(descriptions)

            # 4. 결과 저장 (DB 연결 짧게 사용)
            self.update_status("completed", summary)

        except Exception as e:
            logger.error(f"Processing failed: {e}")
            self.update_status("failed")
