from pydantic import BaseModel, Field, EmailStr, SecretStr
from src.courses.models import UserCategory

class UserSchemaIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    # password: SecretStr

class UserSchemaOut(UserSchemaIn):
    id: int
    category: UserCategory