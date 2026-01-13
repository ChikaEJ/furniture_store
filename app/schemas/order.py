from pydantic import BaseModel, EmailStr

class OrderCreate(BaseModel):
    client_email: EmailStr
    total_price: float

class OrderRead(OrderCreate):
    id: int

    class Config:
        from_attributes = True
