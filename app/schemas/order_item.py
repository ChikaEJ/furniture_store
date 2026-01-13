from pydantic import BaseModel
from typing import Optional

from app.schemas.furniture import FurnitureRead

class OrderItemCreate(BaseModel):
    furniture_id: int
    quantity: int
    price: float


class OrderItemRead(OrderItemCreate):
    id: int
    furniture: Optional[FurnitureRead] = None

    class Config:
        from_attributes = True
