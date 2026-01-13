from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class User(Base):
    __tablename__ = 'user'

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
