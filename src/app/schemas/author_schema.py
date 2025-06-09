from pydantic import BaseModel, Field, EmailStr

class AuthorSchema(BaseModel): # схема добавления автора
	name: str = Field(min_length=2, max_length=50)
	age: int = Field(ge=12, le=120)
	email: EmailStr

