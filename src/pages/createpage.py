from __future__ import annotations as _annotations

import datetime

from fastui.components.display import DisplayMode, DisplayLookup
from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent
from src.config import settings
from datetime import date

navbar_dict = {'Курсы': '/courses/', 'Пользователи':'/users/', 'Помощь': '/help/', 'Войти': '/auth/'}
"""
Navbar demo меню войти если logout иначе имя
"""
footer_dict = {'Github': settings.GITHUB_URL, 'Telegram': settings.TELEGRAM_URL}


def create_page(*components: AnyComponent, title: str | None = None) -> list[AnyComponent]:
    return [
        c.Div(components=[
            c.PageTitle(text=f'{title}' if title else settings.page_title),
            c.Navbar(
                title='Карточки',
                title_event=GoToEvent(url='/'),
                start_links=
                [
                    c.Link(
                        components=[c.Text(text=title)],
                        on_click=GoToEvent(url=url),
                        active=f'startswith:/{title}',
                    ) for title, url in navbar_dict.items()],
                # class_name='.bg-secondary.bg-gradient',
            ),
            c.Page(
                components=[
                    # *((c.Heading(text=title),) if title else ()),
                    *components,
                ],
            ),
            c.Footer(
                extra_text=settings.footer_text + settings.FOOTER_NAME + ', ' + str(date.today().year),
                links=[
                    c.Link(
                        components=[c.Text(text=title)],
                        on_click=GoToEvent(url=url)) for title, url in footer_dict.items()])]
        )
    ]




async def create_table(tablename, prefix: str, fields, alowed) -> AnyComponent:
    return c.Table(
        data=tablename,
        columns=[
            DisplayLookup(field=title, on_click=GoToEvent(url=f'{prefix}'+'/{id}/'))
            for title in fields.__dict__.items()  # if title in alowed.model_fields
        ]
    )
