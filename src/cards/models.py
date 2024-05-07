from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_serializer import SerializerMixin

from src.db.base import Base


class CardsOrm(Base, SerializerMixin):
    __tablename__ = 'cards'

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"))
    user_admin: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str]
    img: Mapped[str | None]    #ссылка на файл
    sound: Mapped[str | None]  #ссылка на файл
    lang_a: Mapped[str]
    lang_b: Mapped[str]