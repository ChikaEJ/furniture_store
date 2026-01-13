from pydantic import BaseModel
from typing import List

from app.schemas.order_item import OrderItemCreate, OrderItemRead


class OrderBase(BaseModel):
    client_email: str


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderRead(OrderBase):

    id: int
    total_price: float
    items: List[OrderItemRead]

    class Config:
        from_attributes = True
