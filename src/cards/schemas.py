from datetime import datetime
from pydantic import BaseModel, Field

class CardsSchemaIn(BaseModel):
    course_id: int = Field(title='Курс ID')
    user_admin: int = Field(title='Администратор')
    name: str = Field(title='Название')
    sound: str = Field(title='Звучание')
    lang_a: str = Field(title='Оригинал')
    lang_b: str = Field(title='Перевод')


class CardsSchema(CardsSchemaIn):
    id: int = Field(title='№')
    course_id: int = Field(title='Курс ID')
    user_admin: int = Field(title='Администратор')
    name: str = Field(title='Название')
    sound: str = Field(title='Звучание')
    lang_a: str = Field(title='Оригинал')
    lang_b: str = Field(title='Перевод')
    created_at: datetime = Field(title='Время создания')
