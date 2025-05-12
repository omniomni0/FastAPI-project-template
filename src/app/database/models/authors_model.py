from database.db import Base, session_factory
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import select

class AuthorsModel(Base): # table "authors" model
	__tablename__ = "authors"

	author_id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	age: Mapped[int]
	email: Mapped[str]

class AuthorsOrm:
	@staticmethod
	async def add_authors(): # add authors to the table
		async with session_factory() as session:
			session.add_all([
				AuthorsModel(name="Shadow_Fiend", age=19, email="nevermore1@mail.com"),
				AuthorsModel(name="Crystal_Maiden", age=21, email="iceicebaby@rambler.com")
			])
			await session.commit()

	@staticmethod
	async def get_authors_as_dict():
		async with session_factory() as session:
			result = await session.execute(select(AuthorsModel))
			authors = result.scalars().all()
			res = {"authors": authors}
			return res
