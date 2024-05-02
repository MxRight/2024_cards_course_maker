from datetime import datetime
from pydantic import BaseModel, Field

class CardsSchemaIn(BaseModel):
    # course_id: int = Field(title='Курс ID')
    # user_admin: int = Field(title='Администратор курса')
    name: str = Field(title='Название карточки')
    sound: str = Field(title='Ссылка на звуковой файл', default='https://')
    img: str = Field(title='Ссылка на изображение', default='https://')
    lang_a: str = Field(title='Содержимое карточки')
    lang_b: str = Field(title='Перевод карточки')

class CardsSchemaIn2(CardsSchemaIn):
    course_id: int = Field(title='Курс ID')
    user_admin: int = Field(title='Администратор курса')
    name: str = Field(title='Название карточки')
    sound: str = Field(title='Ссылка на звуковой файл', default='https://')
    img: str = Field(title='Ссылка на изображение', default='https://')
    lang_a: str = Field(title='Содержимое карточки')
    lang_b: str = Field(title='Перевод карточки')

class CardsSchema(CardsSchemaIn):
    id: int = Field(title='№')
    course_id: int = Field(title='Курс ID')
    user_admin: int = Field(title='Администратор', default=1)
    name: str = Field(title='Название')
    sound: str = Field(title='Ссылка на звуковой файл', default='https://')
    img: str = Field(title='Ссылка на изображение', default='https://')
    lang_a: str = Field(title='Оригинал')
    lang_b: str = Field(title='Перевод')
    created_at: datetime = Field(title='Время создания')

