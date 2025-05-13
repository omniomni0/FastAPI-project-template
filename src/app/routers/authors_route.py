from fastapi import APIRouter
from schemas.author_schema import AuthorSchema
from database.models.authors_model import AuthorsModel, AuthorsOrm
from database.db import session_factory

authors_route = APIRouter(prefix="/authors", tags=["Authors list"])

@authors_route.get("/")
async def get_authors():
	res = await AuthorsOrm.get_authors_as_dict()
	return res


@authors_route.post("/")
async def add_new_author(author: AuthorSchema):
	async with session_factory() as session:
		new_author = AuthorsModel(
			name=author.name,
			age=author.age,
			email=author.email
		)

		session.add(new_author)
		await session.commit()

		return {"succses": True}
