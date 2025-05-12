from pydantic import BaseModel, Field, EmailStr

class AuthorSchema(BaseModel):
	name: str = Field(ge=2, le=50)
	age: int = Field(ge=12, le=120)
	email: EmailStr

