from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayMode, DisplayLookup
from fastui.events import GoToEvent, BackEvent
from src.pages.createpage import create_page, create_table
from src.users.schemas import UserSchemaIn, UserSchemaOut
from src.users.models import User
from src.config import settings
from src.courses.schemas import CourseSchema
from src.orm.orm import AsyncORM
from src.courses.models import CoursesOrm
from src.courses.schemas import CourseSchema
from src.courses.schemas import CourseSchemaIn

go_back = c.Link(components=[c.Text(text='Назад')], on_click=BackEvent())

mainpage = create_page(

    c.Div(
        components=[
            c.Heading(text='Ваш профиль:', level=2),

            c.Markdown(
                text=(
                    'This is a simple unstyled list of links, '
                    'LinkList is also used in `Navbar` and `Pagination`.'
                )
            ),
            c.LinkList(
                links=[
                    c.Link(
                        components=[c.Text(text='Internal Link - the the home page')],
                        on_click=GoToEvent(url='/'),
                    ),
                    c.Link(
                        components=[c.Text(text='Pydantic (External link)')],
                        on_click=GoToEvent(url='https://pydantic.dev'),
                    ),
                    c.Link(
                        components=[c.Text(text='FastUI repo (New tab)')],
                        on_click=GoToEvent(url='https://github.com/pydantic/FastUI', target='_blank'),
                    ),
                ],
            ),
        ],
        class_name='border mt-5 pt-1 shadow-lg p-3 mb-5 bg-body rounded',
    ),
    c.Button(text='Авторизация', on_click=GoToEvent(url='/course/auth/')))


addcourse = create_page(
    go_back,
    c.Heading(text='Создать новый курс', level=2),
    c.ModelForm(
        model=CourseSchemaIn,
        submit_url='/api/course/add',
    ),
)

activecourses = create_page(

)

# editcourse = create_page(
#     go_back,
#     c.Heading(text=f'Редактировать курс: {}', level=2),
#     c.ModelForm(
#         model=CourseSchemaIn,
#         submit_url='/api/course/add',
#     ),
# )

helppage = create_page(
    go_back,
    c.Heading(text='Помощь', level=2),
    c.Image(
        src='',
        # src=settings.logo_src,
        alt='Help', width=100),
    c.Text(text=settings.help_page_text),
)

zeropage = create_page(
    go_back,
c.Heading(text='Вы взломали сайт! За вами выехали!', level=2))
