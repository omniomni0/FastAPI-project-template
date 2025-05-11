from db import Base
from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column

class Gender(Enum):
	male = "male"
	female = "female"

class Authors(Base):
	__tablename__ = "authors"

	user_id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	age: Mapped[int]
	gender: Mapped[Gender]