from typing import Sequence

from sqlalchemy import Row, desc, select

from app.core.db import AsyncSessionLocal
from app.models import Question


class CRUDQuestion:
    @staticmethod
    async def get_list_questions(question_number: int) -> Sequence[Row]:
        async with AsyncSessionLocal() as session:
            questions = await session.execute(
                select(Question)
                .order_by(desc(Question.created_date))
                .limit(question_number)
            )
        return questions.scalars().all()

    @staticmethod
    async def save_questions(questions: list[Question]) -> None:
        async with AsyncSessionLocal() as session:
            list_obj = [
                Question(
                    question_id=question["id"],
                    question_text=question["question"],
                    answer_text=question["answer"],
                )
                for question in questions
            ]
            session.add_all(list_obj)
            await session.commit()


crud_question = CRUDQuestion()
