#
#
#
#
# @router.get('/cities', response_model=FastUI, response_model_exclude_none=True)
# def cities_view(page: int = 1, country: str | None = None) -> list[AnyComponent]:
#     cities = cities_list()
#     page_size = 50
#     filter_form_initial = {}
#     if country:
#         cities = [city for city in cities if city.iso3 == country]
#         country_name = cities[0].country if cities else country
#         filter_form_initial['country'] = {'value': country, 'label': country_name}
#     return demo_page(
#         *tabs(),
#         c.ModelForm(
#             model=FilterForm,
#             submit_url='.',
#             initial=filter_form_initial,
#             method='GOTO',
#             submit_on_change=True,
#             display_mode='inline',
#         ),
#         c.Table(
#             data=cities[(page - 1) * page_size : page * page_size],
#             data_model=City,
#             columns=[
#                 DisplayLookup(field='city', on_click=GoToEvent(url='./{id}'), table_width_percent=33),
#                 DisplayLookup(field='country', table_width_percent=33),
#                 DisplayLookup(field='population', table_width_percent=33),
#             ],
#         ),
#         c.Pagination(page=page, page_size=page_size, total=len(cities)),
#         title='Cities',
#     )