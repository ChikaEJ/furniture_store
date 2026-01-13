from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class OrderItem(Base):
    __tablename__ = "order_items"


    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
    )
    furniture_id: Mapped[int] = mapped_column(
        ForeignKey("furnitures.id", ondelete="RESTRICT"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="items")
    furniture: Mapped["Furniture"] = relationship("Furniture", back_populates="order_items")

from app.models.furniture import Furniture
from app.models.order import Order