from fastapi import APIRouter

articles_route = APIRouter(prefix="/articles", tags=["Articles list"])

@articles_route.get("/")
async def get_articles():

	return {} 
