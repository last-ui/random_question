import asyncio

from fastapi import APIRouter

from app.crud.question import crud_question
from app.schemas.question import QuestionCreate
from app.services.jservice import get_questions_from_api

router = APIRouter()

shared_data = None


@router.post("/", response_model=list[QuestionCreate])
async def create_questions(questions_num: int):
    db_questions = await _read_data(questions_num)
    asyncio.create_task(_create_data(questions_num, db_questions))
    return db_questions


async def _read_data(questions_num: int):
    db_questions = await crud_question.get_list_questions(questions_num)
    return db_questions


async def _create_data(questions_num: int, db_questions):
    if db_questions is not None:
        questions_ids = set([question.id for question in db_questions])
    else:
        questions_ids = []
    questions_from_api = await get_questions_from_api(
        questions_num, questions_ids
    )
    await crud_question.save_questions(questions_from_api)
