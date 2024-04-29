from typing import Annotated

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayLookup, DisplayMode

from fastui.events import GoToEvent
from fastui.forms import fastui_form
from src.pages.pages import mainpage, helppage, addcourse
from src.courses.models import AddCourse, Course
from src.courses.demo_bd import courses as courses_db
from src.users.router import router as users_router
from src.courses.router import router as courses_router
from src.orm.orm import AsyncORM
from src.courses.dbmodel import CoursesOrm
from src.pages.pages import create_page
from src.courses.schemas import CourseSchema, CourseSchemaIn
from src.pages.pages import zeropage
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

"""
Мысли по оформлению:
добавить слева navbar как в степике, с двумя вариантами представления:
на главной странице курсы
на странице курса - этапы

на главной странице: курсы в виде значков слева в навбаре, активный курс если есть, прогресс пользователя, предложение зарегистрироваться или войти

на странице курсы: таблица курсов, добавить новый, добавить курс в избранное

авторизация: ...превращается в профиль

каждый раз при перерисовке главной страницы, 
кидать в случайном порядке svg иконки на образовательную тематику, координаты просчитывать случайным образом

На главной странице при авторизации пользователя активен последний курс который он проходил, с прогрессной шкалой

в ином случае иконки курсов в сетке с названиями, гиперсылка только на иконках

Мысли по логике:
"""


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def draw_main_page() -> list[AnyComponent]:
    return mainpage

@app.post("/api/course/add")
async def add_course(form: Annotated[CourseSchemaIn, fastui_form(CourseSchemaIn)]):
    await AsyncORM.insert_data(CoursesOrm, form)
    return [c.FireEvent(event=GoToEvent(url='/courses/'))]


@app.get("/api/course/add/", response_model=FastUI, response_model_exclude_none=True)
def draw_add_new_course_page() -> list[AnyComponent]:
    return addcourse


@app.get("/api/courses2/", response_model=FastUI, response_model_exclude_none=True)
async def draw_courses_page2() -> list[AnyComponent]:
    res = await AsyncORM.select_data(CoursesOrm, search='', active=True)
    print(res)
    return create_page(
        c.Heading(text='Доступные курсы', level=2),
        # c.FormFieldSelectSearch(),
        *[c.Link(
            active=None, locked=False, mode='tabs',
            components=[c.Image(
                src=i.img if i.img is not None else settings.logo_src,
                alt=i.title, width=80), c.Text(text=i.title)],
            on_click=GoToEvent(url=f'/course/{i.id}/')) for i in res]
        ,
        c.Heading(text='', level=1),
        c.Button(text='Добавить новый курс', on_click=GoToEvent(url='/course/add/')))

@app.get("/api/courses/", response_model=FastUI, response_model_exclude_none=True)
async def draw_courses_page() -> list[AnyComponent]:
    res = await AsyncORM.select_data(CoursesOrm, '', 'all')

    converted_res = [CourseSchema(**i.to_dict()) for i in res]
    # print(converted_res)
    return create_page(
        c.Heading(text='Доступные курсы', level=2),
        # c.FormFieldSelectSearch(),
        c.Table(data=converted_res,
                columns=[
                        DisplayLookup(field='name', table_width_percent=33, on_click=GoToEvent(url='/course/{id}/')),
                         DisplayLookup(field='descr', table_width_percent=33),
                         DisplayLookup(field='user_admin', table_width_percent=33),
                         DisplayLookup(field='category', table_width_percent=33, on_click=GoToEvent(url='/')),
                        DisplayLookup(field='created_at', table_width_percent=33, mode=DisplayMode.date)
                         ]),
        c.Button(text='Добавить новый курс', on_click=GoToEvent(url='/course/add/')))

@app.get("/api/course/{id}/", response_model=FastUI, response_model_exclude_none=True)
async def draw_current_course_page(id: int) -> list[AnyComponent]:
    course = await AsyncORM.select_one(CoursesOrm, id)
    if course is not None:
        return create_page(c.Heading(text=course.name, level=2),
                           c.Heading(text=course.descr, level=4),
                           c.Image(src=course.img if course.img is not None else settings.logo_src,
                                   alt=course.name, width=150),
                           c.Heading(text=' ', level=6),
                           c.Button(text='Начать занятие', on_click=GoToEvent(url='/course/add/')),
                           c.Text(text=' '),
                           c.Button(text='Редактировать курс', on_click=GoToEvent(url='/course/add/')))
    else:
        return zeropage


@app.get("/api/help/", response_model=FastUI, response_model_exclude_none=True)
def draw_help_page() -> list[AnyComponent]:
    return helppage


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='Где я?'))
