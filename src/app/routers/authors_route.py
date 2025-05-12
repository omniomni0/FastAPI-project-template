from fastapi import APIRouter
from schemas.author_schema import AuthorSchema
from database.models.authors_model import AuthorsOrm
from database.db import session_factory

authors_route = APIRouter(prefix="/authors", tags=["Authors list"])

@authors_route.get("/")
async def get_authors():
	return {AuthorsOrm.get_authors_as_dict()}


@authors_route.post("/")
async def add_new_author(author: AuthorSchema):
	async with session_factory() as session:
		session.add(author)
		await session.commit()

	return {"succses": True}
