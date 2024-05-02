from datetime import datetime, date

from pydantic import BaseModel, Field, EmailStr
from src.courses.models import UserCategory, CourseGroup, CourseCategory
from src.courses.models import CoursesOrm

class CourseFilterForm(BaseModel):
    category: str = Field(json_schema_extra={'search_url': '/api/forms/search', 'placeholder': 'Фильтр по категориям'})

class CourseSchemaIn(BaseModel):
    name: str = Field(title='Название курса', default='Курс ..')
    user_admin: int = Field(title='Администратор курса', default=1) #автоматически по входу
    descr: str = Field(title='Описание курса', default="Познай силу ..")
    category: CourseCategory = Field(title='Категория', default=CourseCategory.lang)
    active: bool = Field(title='Активный курс', default=False)
    group: CourseGroup = Field(title='Доступен для групп', default=CourseGroup.free)
class CourseSchema(CourseSchemaIn):
    id: int = Field(title='№')
    name: str = Field(title='Название курса', default='Курс скорописи 17 века')
    user_admin: int = Field(title='Администратор курса', default=1)
    descr: str = Field(title='Описание курса', default="Познай силу РГАДА")
    cards: int = Field(title='Количество карточек')
    category: CourseCategory = Field(title='Категория', default=CourseCategory.lang)
    active: bool = Field(title='Активный курс', default=False)
    group: CourseGroup = Field(title='Доступен для групп', default=CourseGroup.free)
    created_at: datetime = Field(title='Время создания')



