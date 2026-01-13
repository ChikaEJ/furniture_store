from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float
from typing import List

from app.core.database import Base
from app.models.order_items import OrderItem


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_email: Mapped[str] = mapped_column(String(255), nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    items: Mapped[List["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )
