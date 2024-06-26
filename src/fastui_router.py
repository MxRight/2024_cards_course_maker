from typing import Annotated
from functools import cache
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayLookup, DisplayMode
from datetime import datetime
from fastui.events import GoToEvent
from src.pages.pages import mainpage, helppage, addcourse
from src.orm.orm import AsyncORM
from src.courses.models import CoursesOrm
from src.pages.pages import create_page
from src.courses.schemas import CourseSchema, CourseSchemaIn, CourseFilterForm
from src.config import settings
from src.pages.pages import create_page
from src.pages.pages import zeropage
from src.cards.schemas import CardsSchemaIn, CardsSchema
from src.pages.pages import go_back
from src.cards.models import CardsOrm
from src.db.database import get_async_session

router = APIRouter(prefix='/api')


async def lists_of_course(search: str = '', search_in='all'):
    res = await AsyncORM.select_data(CoursesOrm, search, search_in)
    return [CourseSchema(**i.to_dict()) for i in res]

async def lists_of_cards(course_id: int):
    res = await AsyncORM.select_cards(course_id, CardsOrm)
    return [CardsSchema(**i.to_dict()) for i in res]


async def lists_of_course_by_cat(search: str = '', search_in='all'):
    res = await AsyncORM.select_data_by_category(CoursesOrm, search, search_in)
    return [CourseSchema(**i.to_dict()) for i in res]


@router.get("/", response_model=FastUI, response_model_exclude_none=True)
def draw_main_page() -> list[AnyComponent]:
    return mainpage


@router.get("/course/add/", response_model=FastUI, response_model_exclude_none=True)
def draw_add_new_course_page() -> list[AnyComponent]:
    return addcourse

# @router.get("/course/edit/", response_model=FastUI, response_model_exclude_none=True)
# def draw_edit_course_page() -> list[AnyComponent]:
#     return addcourse


@router.get("/courses/", response_model=FastUI, response_model_exclude_none=True)
async def draw_courses_page() -> list[AnyComponent]:
    bd = await lists_of_course()
    return create_page(
        go_back,
        c.Heading(text='Доступные курсы', level=2),
        c.Table(data=bd,
                columns=[
                    DisplayLookup(field='name', table_width_percent=33, on_click=GoToEvent(url='/course/{id}/')),
                    DisplayLookup(field='descr', table_width_percent=33),
                    DisplayLookup(field='cards', table_width_percent=33),
                    DisplayLookup(field='is_active', table_width_percent=33),
                    DisplayLookup(field='creator_name', table_width_percent=33),
                    DisplayLookup(field='category', table_width_percent=33, on_click=GoToEvent(url='/')),
                    DisplayLookup(field='created_at', table_width_percent=33, mode=DisplayMode.date)
                ]),
        c.Button(text='Добавить новый курс', on_click=GoToEvent(url='/course/add/')))


@router.get("/course/{course_id}/cards/", response_model=FastUI, response_model_exclude_none=True)
async def draw_cards_page(course_id: int) -> list[AnyComponent]:
    bd = await lists_of_cards(course_id)
    return create_page(
        go_back,
        c.Heading(text=f'Карточки курса: {course_id}', level=2),   #заменить на имя
        c.Table(data=bd,
                columns=[
                    DisplayLookup(field='name', table_width_percent=33,
                                  on_click=GoToEvent(url=f'/course/{course_id}/cards/' + '{id}/')),
                    DisplayLookup(field='lang_a', table_width_percent=33),
                    DisplayLookup(field='lang_b', table_width_percent=33),
                    # DisplayLookup(field='active', table_width_percent=33),
                    DisplayLookup(field='user_admin', table_width_percent=33),
                    # DisplayLookup(field='category', table_width_percent=33, on_click=GoToEvent(url='/')),
                    DisplayLookup(field='created_at', table_width_percent=33, mode=DisplayMode.date)
                ]),
        c.Button(text='Добавить новый курс', on_click=GoToEvent(url='/course/add/')))

@router.get("/course/{course_id}/add/", response_model=FastUI, response_model_exclude_none=True)
async def draw_current_course_page(course_id: int) -> list[AnyComponent]:
    course = await AsyncORM.select_one(CoursesOrm, course_id)
    if course is not None:
        return create_page(
            go_back,
            c.Heading(text=f'Добавить карточку в курс: "{course.name}"', level=2),
                           c.ModelForm(
                               model=CardsSchemaIn,
                               submit_url=f'/api/cards/{course_id}/add/',
                           ))
@router.get("/course/{course_id}/", response_model=FastUI, response_model_exclude_none=True)
async def draw_current_course_page(course_id: int) -> list[AnyComponent]:
    course = await AsyncORM.select_one(CoursesOrm, course_id)
    if course is not None:
        return create_page(
            go_back,
            c.Heading(text=f'Курс "{course.name}":', level=2),
                           c.Heading(text=course.descr, level=4),
                            c.Heading(text=f'Состоит из {course.cards} карточек. Создатель курса: {course.user_admin}. Создан: {course.created_at.date()}.', level=6),
                           c.Image(src=course.img if course.img is not None else settings.logo_src,
                                   alt=course.name, width=150),
                           c.Heading(text=' ', level=6),
                           c.Button(text='Начать занятие', on_click=GoToEvent(url='/course/begin/')),
                           c.Text(text=' '),
                            c.Button(text='Просмотреть карточки', on_click=GoToEvent(url=f'/course/{course_id}/cards/')),
                            c.Text(text=' '),
                           c.Button(text='Добавить карточку', on_click=GoToEvent(url=f'/course/{course_id}/add/')),
                            c.Text(text=' '),
                            c.Button(text='Редактировать курс', on_click=GoToEvent(url=f'/course/{course_id}/edit/'))
                           )
    else:
        return zeropage


@router.get("/help/", response_model=FastUI, response_model_exclude_none=True)
def draw_help_page() -> list[AnyComponent]:
    return helppage



