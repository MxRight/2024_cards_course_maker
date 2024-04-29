code1 = """
@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def users_table() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Image(src='https://i.ytimg.com/vi/T7c4kfYKdNU/mqdefault.jpg', alt='Logo', width=100),
                c.Heading(text='Пользователи', level=2),
                c.Code(text=''),
                c.Table(
                    data=users,

                    columns=[
                        DisplayLookup(field='id', on_click=GoToEvent(url='/user/{id}/')),
                        DisplayLookup(field='name', on_click=GoToEvent(url='/user/{id}/')),
                        DisplayLookup(field='dob', mode=DisplayMode.date),
                    ],
                ),
                c.Button(text='Города', on_click=GoToEvent(url='/main/')),
                c.Button(text='User 2', on_click=GoToEvent(url='/user/2/')),
                c.Button(text='print', on_click=print('Hello')),
            ]
        ),
    ]
                """