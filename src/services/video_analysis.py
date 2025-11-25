import asyncio
import base64
import io
import logging
import urllib.parse
import uuid

import cv2
import edge_tts
import httpx
import yt_dlp

# 분리된 모듈 import
from src.core.config import settings
from src.core.database import session_local_write
from src.core.message_broker import kafka_producer
from src.core.storage import storage_client
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

    async def complete_analysis(self, summary, thumbnail_url, audio_url):
        db = self._get_db()
        video_title = "Unknown Video"
        try:
            video = db.query(Video).filter(Video.id == self.video_id).first()
            if video:
                video.analysis_status = "completed"
                video.ai_summary = summary
                video_title = video.title

                if thumbnail_url:
                    video.thumbnail = thumbnail_url
                    video.is_ai_thumbnail = True

                if audio_url:
                    video.ai_audio = audio_url

                db.commit()
                logger.info(
                    f"Analysis Completed. Thumb: {bool(thumbnail_url)}, Audio: {bool(audio_url)}"
                )
        except Exception as e:
            db.rollback()
            logger.error(f"DB Update failed: {e}")
        finally:
            db.close()

        # 알림 이벤트 발행
        try:
            notification_message = {
                "event": "analysis_completed",
                "video_id": self.video_id,
                "title": video_title,
                "status": "completed",
                "summary_preview": summary[:100] + "..." if summary else "No summary",
            }
            # 설정된 토픽이 없으면 기본값 사용
            topic = getattr(settings, "KAFKA_TOPIC_NOTIFICATION", "video-notifications")
            await kafka_producer.send_message(topic, notification_message)
        except Exception as e:
            logger.error(f"Failed to send notification event: {e}")

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
        prompt = "Describe this image in detail."
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(
                    f"{settings.OLLAMA_URL}/api/generate",
                    json={
                        "model": "minicpm-v:8b",
                        "prompt": prompt,
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
        """이미지 생성을 위한 영문 프롬프트 요청"""
        try:
            prompt_instruction = (
                f"Based on the summary below, write a high-quality text-to-image prompt "
                f"for a movie poster style thumbnail. Write ONLY the English prompt.\n\nSummary: {summary}"
            )
            async with httpx.AsyncClient(timeout=60.0) as client:
                resp = await client.post(
                    f"{settings.OLLAMA_URL}/api/generate",
                    json={
                        "model": "exaone3.5:latest",
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
        raw_prompt = await self.generate_thumbnail_prompt(summary)
        if not raw_prompt:
            return None

        clean_prompt = (
            raw_prompt.replace("**", "")
            .replace('"', "")
            .replace("Movie Poster Thumbnail Prompt:", "")
            .strip()
        )

        try:
            encoded_prompt = urllib.parse.quote(f"cinematic shot, masterpiece, {clean_prompt}")

            # [수정] 모델 Fallback 로직 추가
            # 1. Flux 모델 시도
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1280&height=720&model=flux&seed=42"

            async with httpx.AsyncClient(timeout=45.0) as client:
                resp = await client.get(image_url)

                if resp.status_code != 200:
                    return None
                image_data = io.BytesIO(resp.content)  # 파일 객체로 변환

                # Flux 실패 시 Turbo 모델로 재시도
                if resp.status_code != 200:
                    logger.warning(
                        f"Flux model failed ({resp.status_code}). Retrying with Turbo model..."
                    )
                    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1280&height=720&model=turbo&seed=42"
                    resp = await client.get(image_url)

                if resp.status_code != 200:
                    logger.error(f"Image generation failed finally: {resp.text}")
                    return None

                image_data = io.BytesIO(resp.content)

            filename = f"ai_thumb_{self.video_id}_{uuid.uuid4().hex[:8]}.jpg"
            return storage_client.upload_file(image_data, object_name=filename)

        except Exception as e:
            logger.error(f"Thumbnail generation/upload failed: {e}")
            return None

    async def generate_and_upload_audio(self, text: str) -> str:
        """텍스트를 음성(MP3)으로 변환하여 MinIO에 업로드"""
        if not text:
            return None

        try:
            communicate = edge_tts.Communicate(text, "ko-KR-SunHiNeural")
            audio_buffer = io.BytesIO()
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_buffer.write(chunk["data"])
            audio_buffer.seek(0)

            filename = f"ai_audio_{self.video_id}_{uuid.uuid4().hex[:8]}.mp3"
            s3_url = storage_client.upload_file(
                audio_buffer, object_name=filename, content_type="audio/mpeg"
            )
            logger.info(f"TTS Audio generated in memory: {s3_url}")
            return s3_url
        except Exception as e:
            logger.error(f"TTS generation/upload failed: {e}")
            return None

    async def process_video(self):
        # 1. 상태 업데이트 (DB 연결 짧게 사용)
        self.update_status("processing")
        logger.info(f"Starting analysis for Video {self.video_id}")

        url = None
        # 2. URL 조회 (DB 연결 짧게 사용)
        db = self._get_db()
        url = db.query(Video.url).filter(Video.id == self.video_id).scalar()
        db.close()
        if not url:
            self.update_status("failed")
            return

        try:
            frames = self.extract_keyframes(url)
            if not frames:
                raise Exception("No frames extracted")
            descs = []
            for frame in frames:
                d = await self.generate_image_description(frame)
                if d:
                    descs.append(d)

            summary = await self.summarize_descriptions(descs)

            if not summary or summary == "Failed":
                raise Exception("Summary generation failed")

            # 병렬 실행
            ai_thumb_task = self.generate_and_upload_thumbnail(summary)
            ai_audio_task = self.generate_and_upload_audio(summary)

            ai_thumb_url, ai_audio_url = await asyncio.gather(ai_thumb_task, ai_audio_task)

            await self.complete_analysis(summary, ai_thumb_url, ai_audio_url)

        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            self.update_status("failed")
