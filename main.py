from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import prebuilt_html, components as c

from fastui.events import GoToEvent
from fastui.forms import fastui_form
from src.api.users import router as users_router
from src.api.courses import router as courses_router
from src.api.cards import router as cards_router
from src.orm.orm import AsyncORM
from src.courses.models import CoursesOrm
from src.cards.models import CardsOrm

from src.courses.schemas import CourseSchemaIn
from src.fastui_router import router as fastui_router
from src.cards.schemas import CardsSchemaIn, CardsSchemaIn2

temp_admin = 1
# временное id админа, после добавления авторизации брать оттуда

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"]

app = FastAPI(title='Карточки')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users_router)
app.include_router(courses_router)
app.include_router(cards_router)

app.include_router(fastui_router)




@app.post("/api/course/add/")
async def add_course(form: Annotated[CourseSchemaIn, fastui_form(CourseSchemaIn)]):
    await AsyncORM.insert_data(CoursesOrm, form)
    return [c.FireEvent(event=GoToEvent(url='/courses/'))]

@app.post("/api/cards/{course_id}/add/")
async def add_card(course_id: int, form: Annotated[CardsSchemaIn, fastui_form(CardsSchemaIn)]):
    add_dict = {'course_id': course_id, 'user_admin': temp_admin}
    add_dict.update(form.dict())
    updated_form = CardsSchemaIn2(**add_dict)
    await AsyncORM.insert_data(CardsOrm, updated_form)
    #добавить в курсе +1 к количеству карточек (или пересчитать их позже?)
    return [c.FireEvent(event=GoToEvent(url=f'/course/{course_id}/'))]


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='Где я?'))