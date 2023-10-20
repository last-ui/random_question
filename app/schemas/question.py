from datetime import datetime

from pydantic import BaseModel


class QuestionCreate(BaseModel):
    id: int
    question_id: int
    question_text: str
    answer_text: str
    created_date: datetime

    class Config:
        from_attributes = True
