from pydantic import BaseModel, Field
from pydantic.types import Enum

class CourseCategory(Enum):
    languages: str = 'Языки'
    history: str = 'История'
    math: str = 'Математика'
    other: str = 'Другое'
class Course(BaseModel):
    id: int = Field(title='№') # скрытое поле
    title: str = Field(title='Название курса')
    descr: str = Field(title='Описание курса')
    category: CourseCategory = Field(title='Категория') #языки, история, математика и т.д.
    active: bool = Field(title='Активный курс') #виден только создателю или всем пользователям
    group: int = Field(title='Доступен для групп') #доступность для определенных груп пользователей, например vip оплатившие подписку


class AddCourse(BaseModel):
    title: str = Field(title='Название курса')
    descr: str = Field(title='Описание курса')
    category: CourseCategory = Field(title='категория', default='Языки')
    active: bool = Field(title='Активный курс', default=False)
    group: bool = Field(title='Доступен для всех типов пользователей', default=True)