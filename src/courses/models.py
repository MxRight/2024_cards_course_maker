from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.db.base import Base
from enum import Enum
from sqlalchemy_serializer import SerializerMixin


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
    creator_name: Mapped[str]
    img: Mapped[str | None]
    name: Mapped[str]
    descr: Mapped[str]
    category: Mapped[CourseCategory]
    cards: Mapped[int] = mapped_column(default=0)  # количество карточек в курсе, пересчитывать при изм.
    group: Mapped[CourseGroup]
