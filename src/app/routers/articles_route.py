from fastapi import APIRouter
from schemas.article_schema import ArticleSchema
from database.models.articles_model import ArticlesModel, ArticlesOrm
from database.db import session_factory
articles_route = APIRouter(prefix="/articles", tags=["Articles list"]) # роутер для статей

@articles_route.get("/", name="Get articles as json")
async def get_articles():
	res = await ArticlesOrm.get_articles_as_dict()
	return res 

@articles_route.post("/", name="Add new article")
async def add_new_article(article: ArticleSchema):
	async with session_factory() as session:
		
		new_article = ArticlesModel(
			title=article.title,
			author_id=article.author_id,
			body=article.body
		)

		session.add(new_article)
		await session.commit()

		return {"ok": True}
