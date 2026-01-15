from pydantic import BaseModel, EmailStr

from app.schemas.order_item import OrderItemCreate, OrderItemRead


class OrderBase(BaseModel):
    client_email: EmailStr


class OrderCreate(OrderBase):
    items: list[OrderItemCreate]


class OrderRead(OrderBase):
    id: int
    total_price: float
    items: list[OrderItemRead]

    class Config:
        from_attributes = True
