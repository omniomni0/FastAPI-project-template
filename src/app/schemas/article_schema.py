from pydantic import BaseModel, Field

class ArticleSchema(BaseModel):
	title: str = Field(min_length=5, max_length=150)
	author: str # тут надо будет добилить отношение между таблицами, на потом
	body: str = Field(min_length=15, max_length=5000)



