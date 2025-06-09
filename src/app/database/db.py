from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config_db import Settings
settings = Settings() # type: ignore
class Base(DeclarativeBase):
	pass

engine = create_async_engine( # движок для бд
	url=settings.__repr__(),
	echo=True
)
session_factory = async_sessionmaker(engine, expire_on_commit=False) # фабрика сессий, нужна для рабоиты с бд

async def create_tables(): # создаём таблицы
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)