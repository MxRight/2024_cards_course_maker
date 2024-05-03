from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from sqlalchemy_serializer import SerializerMixin

from src.courses.models import Base

"""
Необходимо реализовать:
прогресс пользователя

можно попробовать реализовать принцип подписки/покупки доступа к курсу
полное открытие курса или доступ ко всем курсам до определенной даты

"""


class UserOrm(SQLAlchemyBaseUserTable[int], Base, SerializerMixin):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )


class UserProgress:
    courses: dict
    courses_time: dict
    """
    словарь в котором ключи - id курсов проходимые пользователем, 
    значения - словарь в котором ключи - id карточек, значения - цифра, 
    сколько раз надо повторить карточку, при неудачной попытке прибавляется например 3
    если значене 0, то карточка считается выученной,
    стоит ли добавить дату, и со временем прибавлять к значениям карточек еденицы для повторения?
    courses = {1:{1:5, 2:0, 3:1}}
    """