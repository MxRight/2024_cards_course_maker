from typing import Annotated
from functools import cache
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayLookup, DisplayMode

from fastui.events import GoToEvent
from fastui.forms import fastui_form
from src.pages.pages import mainpage, helppage, addcourse
from src.users.router import router as users_router
from src.courses.router import router as courses_router
from src.orm.orm import AsyncORM
from src.courses.models import CoursesOrm

from src.courses.schemas import CourseSchema, CourseSchemaIn, CourseFilterForm
from src.fastui_router import router as fastui_router
from src.config import settings

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
app.include_router(fastui_router)




@app.post("/api/course/add")
async def add_course(form: Annotated[CourseSchemaIn, fastui_form(CourseSchemaIn)]):
    await AsyncORM.insert_data(CoursesOrm, form)
    return [c.FireEvent(event=GoToEvent(url='/courses/'))]


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='Где я?'))