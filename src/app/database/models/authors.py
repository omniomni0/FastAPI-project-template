from db import Base
from sqlalchemy.orm import Mapped, mapped_column

class Authors(Base):
	__tablename__ = "authors"

	author_id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	age: Mapped[int]
	email: Mapped[str]