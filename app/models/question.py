from sqlalchemy import Column, DateTime, Integer, Text

from app.core.db import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    text = Column(
        Text,
    )
    answer_text = Column(
        Text,
    )
    created_date = Column(DateTime)
