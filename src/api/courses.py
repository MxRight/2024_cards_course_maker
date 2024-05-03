from fastapi import APIRouter, status
from src.orm.orm import AsyncORM
from src.courses.schemas import CourseSchemaIn
from src.courses.models import CoursesOrm

router = APIRouter(tags=["Курсы"], prefix='/api/courses')


# @router.post("/add/", response_model=UserSchemaOut, status_code=status.HTTP_201_CREATED)
@router.post("/add/", status_code=status.HTTP_201_CREATED)
async def add_new_course(course: CourseSchemaIn):
    new_course = AsyncORM.insert_data(CoursesOrm, course)
    return await new_course

@router.get("/all/")
async def select_all_user():
    list_of_courses = AsyncORM.select_data(CoursesOrm)
    return await list_of_courses
