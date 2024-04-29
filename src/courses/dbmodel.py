from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, LargeBinary
from src.db.database import Base
from enum import Enum
from pydantic import EmailStr
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin


"""
Необходимо реализовать:
прогресс пользователя

можно попробовать реализовать принцип подписки/покупки доступа к курсу
полное открытие курса или доступ ко всем курсам до определенной даты

"""

class UserCategory(Enum):
    superuser = 'Главный админ'
    admin = 'Администратор'
    user = 'Пользователь'

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


class UserOrm(Base, SerializerMixin):
    __tablename__ = 'users'

    name: Mapped[str]
    password: Mapped[str]  #заменить на хэш
    email: Mapped[str]
    category: Mapped[UserCategory] = mapped_column(default='user')
    # user_progress: Mapped[dict]


class CourseCategory(Enum):
    lang = 'Языки'
    history = 'История'
    other = 'Другое'

class CourseGroup(Enum):
    free = 'бесплатный'
    paid = 'платный'



class CoursesOrm(Base, SerializerMixin):
    __tablename__ = 'courses'

    user_admin: Mapped[int] = mapped_column(ForeignKey("users.id"))
    img: Mapped[str | None]
    name: Mapped[str]
    descr: Mapped[str]
    category: Mapped[CourseCategory]
    cards: Mapped[int] = mapped_column(default=0) #количество карточек в курсе, пересчитывать при изм.
    group: Mapped[CourseGroup]



class CardsOrm(Base, SerializerMixin):
    __tablename__ = 'cards'

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"))
    user_admin: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str]
    img: Mapped[str | None]    #ссылка на файл
    sound: Mapped[str | None]  #ссылка на файл
    lang_a: Mapped[str]
    lang_b: Mapped[str]
