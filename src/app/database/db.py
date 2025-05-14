from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config_db import settings
class Base(DeclarativeBase):
	pass

engine = create_async_engine(
	url=settings.DB_URL,
	echo=True
)
session_factory = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)