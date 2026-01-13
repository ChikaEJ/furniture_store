from app.core.database import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float
from enum import Enum

from app.models.order_items import OrderItem


class FurnitureCategory(str, Enum):
    TABLE = "table"
    CHAIR = "chair"
    SOFA = "sofa"


class Furniture(Base):
    __tablename__ = "furnitures"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category: Mapped[FurnitureCategory] = mapped_column(nullable=False)

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="furniture"
    )
