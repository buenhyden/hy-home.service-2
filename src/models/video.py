from sqlalchemy import Column, Integer, String, Text

from src.core.database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    analysis_status = Column(String)
    ai_summary = Column(Text)

    # 워커에서 필요하다면 추가 필드 정의 가능
