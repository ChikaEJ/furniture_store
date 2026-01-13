from pydantic import BaseModel

from app.schemas.enums import FurnitureCategory


class FurnitureCreate(BaseModel):
    name: str
    price: float
    category: FurnitureCategory

class FurnitureRead(FurnitureCreate):
    id: int

    class Config:
        from_attributes = True