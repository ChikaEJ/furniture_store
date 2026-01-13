from typing import List
from sqlalchemy import Enum as SQLEnam
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.schemas.enums import FurnitureCategory


class Furniture(Base):
    __tablename__ = "furnitures"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category: Mapped[FurnitureCategory] = mapped_column(SQLEnam(FurnitureCategory), nullable=False)

    order_items: Mapped[List["OrderItem"]] = relationship(
        "OrderItem",
        back_populates="furniture"
    )

from app.models.order_item import OrderItem
