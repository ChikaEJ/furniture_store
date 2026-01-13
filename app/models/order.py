from typing import List

from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Order(Base):
    __tablename__ = "orders"

    client_email: Mapped[str] = mapped_column(String(255), nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    items: Mapped[List["OrderItem"]] = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
    )

from app.models.order_item import OrderItem
