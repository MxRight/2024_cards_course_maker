from pydantic import BaseModel, Field, EmailStr, SecretStr


class UserSchemaIn(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str
    # password: SecretStr

class UserSchemaOut(UserSchemaIn):
    id: int
