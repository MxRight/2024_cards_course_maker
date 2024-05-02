from fastapi import APIRouter, status
from src.orm.orm import AsyncORM
from src.courses.models import CardsOrm

router = APIRouter(tags=["Карточки"], prefix='/api/cards')



@router.post("/add/", status_code=status.HTTP_201_CREATED)
async def add_new_card(card: CourseSchemaIn):
    new_card = AsyncORM.insert_data(CardsOrm, card)
    return await new_card

@router.get("/all/")
async def select_all_cards(course_id: int):
    #выбрать все карточки указанного курса
    list_of_cards = AsyncORM.select_data(CardsOrm)
    return await list_of_cards
