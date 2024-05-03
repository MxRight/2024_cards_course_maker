from fastapi import APIRouter, status
from src.orm.orm import AsyncORM
from src.cards.models import CardsOrm
from src.cards.schemas import CardsSchemaIn

router = APIRouter(tags=["Карточки"], prefix='/api/cards')



@router.post("/add/", status_code=status.HTTP_201_CREATED)
async def add_new_card(card: CardsSchemaIn):
    new_card = AsyncORM.insert_data(CardsOrm, card)
    return await new_card

@router.get("/all/")
async def select_all_cards(course_id: int):
    #выбрать все карточки указанного курса
    list_of_cards = AsyncORM.select_cards(course_id, CardsOrm)
    return await list_of_cards
