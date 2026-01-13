from sqlalchemy import ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.furniture import Furniture
from app.models.order import Order


class OrderItem(Base):
    __tablename__ = "order_items"

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id", ondelete="CASCADE")
    )
    furniture_id: Mapped[int] = mapped_column(
        ForeignKey("furnitures.id")
    )

    quantity: Mapped[int] = mapped_column(Integer, default=1)
    price_at_purchase: Mapped[float] = mapped_column(Float, nullable=False)

    order: Mapped["Order"] = relationship(back_populates="items")
    furniture: Mapped["Furniture"] = relationship(back_populates="order_items")
