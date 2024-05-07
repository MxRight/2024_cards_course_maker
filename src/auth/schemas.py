from pydantic import BaseModel, Field, EmailStr, SecretStr
from fastapi_users import schemas


class UserSchemaRead(schemas.BaseUser[int]):
    # id: models.ID
    name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserSchemaCreate(schemas.BaseUserCreate):
    name: str
    email: EmailStr
    password: str
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False


class UserUpdate(schemas.BaseUserUpdate):
    name: str | None = None
    password: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None
    is_verified: bool | None = None
