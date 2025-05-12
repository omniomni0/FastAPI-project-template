from datetime import datetime
from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text

class ArticlesModel(Base): # table "articles" model
	__tablename__ = "articles"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str]
	created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
	author: Mapped[str]
	body: Mapped[str]
