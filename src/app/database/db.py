from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config_db import settings

engine = create_async_engine(
	url=settings.DB_URL,
	echo=True
)
session_factory = async_sessionmaker(engine)

class Base(DeclarativeBase):
	pass