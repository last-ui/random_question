from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Text

from app.core.db import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, unique=True)
    question_text = Column(Text)
    answer_text = Column(Text)
    created_date = Column(DateTime, default=datetime.now)
