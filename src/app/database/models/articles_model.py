from datetime import datetime
from database.db import Base, session_factory
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, select

class ArticlesModel(Base): # table "articles" model
	__tablename__ = "articles"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
	author_id: Mapped[int] # надо доделать, тут нужно отношение мужду таблицами
	body: Mapped[str]

class ArticlesOrm:
	@staticmethod
	async def add_articles(): # add authors to the table
		async with session_factory() as session:
			session.add_all([ArticlesModel(
				author_id=1, 
				title="Почему дл имба",
				body="""ну крч значит закупаемся в начале, лупим крипов и сразу после птшек берем дл"""
				),
				
				ArticlesModel(
				author_id=2, 
				title="Сборка через глимер хуйня", 
				body="""Не, внатуре глимер ваще хуета та еще, берите шб, качайте до сильвера и не парьтесь хули""")
			])
			await session.commit()

	@staticmethod
	async def get_articles_as_dict():
		async with session_factory() as session:
			result = await session.execute(select(ArticlesModel))
			articles = result.scalars().all()
			res = {"articles": articles}
			return res
