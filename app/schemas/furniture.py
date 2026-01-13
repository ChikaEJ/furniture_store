from pydantic import BaseModel


class FurnitureCreate(BaseModel):
    title: str
    price: float
    category_id: int

class FurnitureRead(FurnitureCreate):
    id: int

    class Config:
        from_attributes = True