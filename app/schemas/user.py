from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str

class UserRead(UserCreate):
    id: int

    class Config:
        from_attributes = True