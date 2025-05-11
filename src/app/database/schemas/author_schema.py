from pydantic import BaseModel, Field, EmailStr

# схемы авторов
class AuthorCreate(BaseModel):
	name: str
	age: int = Field(ge=12, le=120)
	email: EmailStr

class AuthorRead(AuthorCreate):
	id: int

	class Config: # Небольшая настройка, чтобы Алхимия видела схему автора
		orm_mode = True