from typing import Annotated
from functools import cache
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayLookup, DisplayMode

from fastui.events import GoToEvent

from src.pages.pages import mainpage, helppage, addcourse

from src.orm.orm import AsyncORM
from src.courses.models import CoursesOrm
from src.pages.pages import create_page
from src.courses.schemas import CourseSchema, CourseSchemaIn, CourseFilterForm
from src.pages.pages import zeropage
from src.config import settings
from src.pages.pages import create_page
from src.pages.pages import zeropage

router = APIRouter(prefix='/api')


async def lists_of_course(search: str = '', search_in=True):
    res = await AsyncORM.select_data(CoursesOrm, search, search_in)
    return [CourseSchema(**i.to_dict()) for i in res]


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
        c.Heading(text='Доступные курсы', level=2),
        c.Table(data=bd,
                columns=[
                    DisplayLookup(field='name', table_width_percent=33, on_click=GoToEvent(url='/course/{id}/')),
                    DisplayLookup(field='descr', table_width_percent=33),
                    DisplayLookup(field='cards', table_width_percent=33),
                    DisplayLookup(field='active', table_width_percent=33),
                    DisplayLookup(field='user_admin', table_width_percent=33),
                    DisplayLookup(field='category', table_width_percent=33, on_click=GoToEvent(url='/')),
                    DisplayLookup(field='created_at', table_width_percent=33, mode=DisplayMode.date)
                ]),
        c.Button(text='Добавить новый курс', on_click=GoToEvent(url='/course/add/')))


@router.get("/course/{id}/", response_model=FastUI, response_model_exclude_none=True)
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


@router.get("/help/", response_model=FastUI, response_model_exclude_none=True)
def draw_help_page() -> list[AnyComponent]:
    return helppage



