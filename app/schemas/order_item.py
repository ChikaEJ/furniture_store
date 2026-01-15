from pydantic import BaseModel, Field

class OrderItemCreate(BaseModel):
    furniture_id: int
    quantity: int = Field(gt=0)


class OrderItemRead(BaseModel):
    furniture_id: int
    quantity: int
    price: float

    class Config:
        from_attributes = True
