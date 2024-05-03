from fastui import components as c
from fastui.events import GoToEvent, BackEvent
from src.pages.createpage import create_page
from src.config import settings
from src.courses.schemas import CourseSchemaIn

go_back = c.Link(components=[c.Text(text='Назад')], on_click=BackEvent())

mainpage = create_page(

    c.Div(
        components=[
            c.Heading(text='Ваш профиль:', level=2),

            c.Markdown(
                text=(
                    'Ваши `прогресс` и `избранное`:'
                )
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
        submit_url='/api/course/add/',
    ),
)

# addcard = create_page(
#     go_back,
#     c.Heading(text='Создать новый курс', level=2),
#     c.ModelForm(
#         model=CourseSchemaIn,
#         submit_url='/api/course/add',
#     ),
# )

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
