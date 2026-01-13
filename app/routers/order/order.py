from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud.order import order_crud
from app.core.database import get_db
from app.models.order import Order
from app.schemas.order import OrderRead, OrderCreate

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/", response_model=List[OrderRead])
async def get_orders_by_email(email: str, db: AsyncSession = Depends(get_db)) -> List[OrderRead]:
    return await order_crud.get_orders_by_email(email=email, db=db)

@router.post("/", response_model=OrderRead)
async def create_order(data: OrderCreate, db: AsyncSession = Depends(get_db)):
    order = await order_crud.create_order(data=data, db=db)

    return order