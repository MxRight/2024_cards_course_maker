from fastapi import APIRouter, status
from src.orm.orm import AsyncORM
from src.auth.schemas import UserSchemaRead
from src.auth.models import UserOrm

router = APIRouter(tags=["Пользователи"], prefix='/api/users')



@router.post("/add/", status_code=status.HTTP_201_CREATED)
async def add_new_user(user: UserSchemaRead):
    new_user = AsyncORM.insert_data(UserOrm, user)
    return await new_user

@router.get("/all/")
async def select_all_user():
    list_of_users = AsyncORM.select_data(UserOrm)
    return await list_of_users


# @router.get("/resumes", tags=["Резюме"])
# async def get_resumes():
#     resumes = await AsyncORM.select_resumes_with_all_relationships()
#     return resumes


#
# @router.get("/", response_model=list[Product])
# async def get_products(
#     session: AsyncSession = Depends(databasehelper.scoped_session_dependency),
# ):
#     return await crud.get_products(session=session)
#
#
# @router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
# async def create_product(
#     product_in: ProductCreate,
#     session: AsyncSession = Depends(databasehelper.scoped_session_dependency),
# ):
#     return await crud.crate_product(session=session, product_in=product_in)
#
#
# @router.get("/{product_id}", response_model=Product)
# async def get_product(product: Product = Depends(get_product_by_id)):
#     return product
#
#
# @router.put("/{product_id}")
# async def update_product(
#     product_update: ProductUpdate,
#     product: Product = Depends(get_product_by_id),
#     session: AsyncSession = Depends(databasehelper.scoped_session_dependency),
# ):
#     return await crud.update_product(
#         session=session, product=product, product_update=product_update
#     )
#
#
# @router.patch("/{product_id}")
# async def update_product_partial(
#     product_update: ProductUpdatePartical,
#     product: Product = Depends(get_product_by_id),
#     session: AsyncSession = Depends(databasehelper.scoped_session_dependency),
# ):
#     return await crud.update_product(
#         session=session, product=product, product_update=product_update, partial=True
#     )
#
#
# @router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_product(
#     product: Product = Depends(get_product_by_id),
#     session: AsyncSession = Depends(databasehelper.scoped_session_dependency),
# ) -> None:
#     await crud.delete_product(product=product, session=session)
