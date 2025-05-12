from fastapi import FastAPI
from database.models.authors_model import AuthorsOrm
from routers.authors_route import authors_route
from database.db import create_tables
# from routers.articles_route import articles_route
import uvicorn
import asyncio
app = FastAPI()
app.include_router(authors_route)

@app.get("/")
async def root():
	return {"data": "Welcome to the Main Page!"}


async def main():
	await create_tables()
	await AuthorsOrm.add_authors()
	uvicorn.run("main:app", reload=True)



if __name__ == "__main__":
	asyncio.run(main())

