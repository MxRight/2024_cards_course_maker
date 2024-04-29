from pydantic import BaseModel, Field
from datetime import date


class User(BaseModel):
    id: int = Field(title='№')
    name: str = Field(title='Имя')
    dob: date = Field(title='День рождения')

class UserFilterForm(BaseModel):
    name: str = Field(json_schema_extra={'search_url': '/api/forms/search', 'placeholder': 'Filter by Name...'})



