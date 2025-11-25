import asyncio
import json

from aiokafka import AIOKafkaConsumer

# src 모듈 경로 인식 (필요시)
# sys.path.append("...")
from src.core.config import settings
from src.core.logger import AppLogger
from src.services.video_analysis import VideoAnalysisService

# ---------------------------------------------------------
# Logging 설정
# ---------------------------------------------------------
app_logger = AppLogger(logger_name="worker.main")
logger = app_logger.setup(
    service_name=settings.PROJECT_NAME,
    loki_url=settings.LOKI_URL,
    enable_console=True,
    enable_file=True,
    enable_loki=False,
)


async def consume():
    consumer = AIOKafkaConsumer(
        settings.KAFKA_TOPIC_ANALYSIS,
        bootstrap_servers=settings.KAFKA_BROKERS,
        group_id=settings.KAFKA_GROUP_ID,
        auto_offset_reset="earliest",
    )

    await consumer.start()
    logger.info(f"Worker started. Listening on {settings.KAFKA_TOPIC_ANALYSIS}...")

    try:
        async for msg in consumer:
            try:
                payload = json.loads(msg.value.decode("utf-8"))
                video_id = payload.get("video_id")
                trace_id = payload.get("trace_id")

                logger.info(f"Received task for Video ID: {video_id} (Trace: {trace_id})")

                # [수정] DB 세션을 밖에서 주입하지 않고, ID만 전달
                service = VideoAnalysisService(video_id)
                await service.process_video()

            except Exception as e:
                logger.error(f"Error processing message: {e}")

    finally:
        await consumer.stop()


if __name__ == "__main__":
    asyncio.run(consume())
