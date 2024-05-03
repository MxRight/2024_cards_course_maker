from sqlalchemy import select
from src.db.database import async_session_factory
from src.courses.models import CoursesOrm
from src.cards.models import CardsOrm
from src.auth.models import UserOrm


class AsyncORM:
    @staticmethod
    async def insert_data(model, data) -> UserOrm | CoursesOrm | CardsOrm:
        async with async_session_factory() as session:
            insert = model(**data.model_dump())
            session.add(insert)
            # flush взаимодействует с БД, поэтому пишем await
            # await session.flush()
            await session.commit()
            return insert
            # return UserSchemaOut(**insert.model_dump())

    @staticmethod
    async def select_data(model, search='', active='all'):
        """
        :param search: строка для поиска в выборке, чувствительна к регистру
        :param model:
        :param active True | False | 'all' Флаг выборки: только активные/ только неактивные или все курсы/карточки/пользователи
        :return:
        """
        async with async_session_factory() as session:
            if active == 'all':
                query = select(model).filter(model.name.like(f'%{search}%')).order_by(-model.id)
                # order_by -1 от нового к старому

            else:
                query = select(model).filter(model.name.like(f'%{search}%')).where(model.active == active).order_by(
                    -model.id)
            result = await session.execute(query)
            data = result.scalars().all()
            return list(data)

    @staticmethod
    async def select_data_by_category(model, search='', active='all'):
        async with async_session_factory() as session:
            if active == 'all':
                query = select(model).where(model.category == search).order_by(-model.id)

            else:
                query = select(model).where(model.category == search).where(model.active == active).order_by(
                    -model.id)
            result = await session.execute(query)
            data = result.scalars().all()
            return list(data)

    @staticmethod
    async def select_one(model, record_id: int):
        async with async_session_factory() as session:
            return await session.get(model, record_id)

    @staticmethod
    async def select_cards(course_id: int, model=CardsOrm):
        async with async_session_factory() as session:
            query = select(model).where(model.course_id == course_id).order_by(-model.id)
            result = await session.execute(query)
            data = result.scalars().all()
            return list(data)

    #
    # @staticmethod
    # async def update_data(id_record: int, new_username: str = "Misha"):
    #     async with async_session_factory() as session:
    #         worker_michael = await session.get(WorkersOrm, worker_id)
    #         worker_michael.username = new_username
    #         await session.refresh(worker_michael)
    #         await session.commit()
