from typing import Dict, Any

from fastapi import HTTPException
from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud.base_crud import BaseCRUD
from app.models.furniture import Furniture
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.order import OrderRead, OrderCreate


class OrderCRUD(BaseCRUD):
    async def get_orders_by_email(
            self, email: str, db: AsyncSession
    ) -> list[OrderRead]:
        result = await db.execute(
            select(Order)
            .where(Order.client_email == email)
            .options(
                selectinload(
                    Order.items
                ).selectinload(Furniture)).order_by(Order.id))

        orders = result.scalars().all()

        return [
            OrderRead(
                id=order.id,
                client_email=order.client_email,
                total_price=order.total_price,
                items=[item.furniture_id for item in order.items]
            )
            for order in orders
        ]

    async def create_order(self, data: OrderCreate, db: AsyncSession) -> Order:
        furniture_ids = {item.furniture_id for item in data.items}

        result = await db.execute(
            select(Furniture).where(Furniture.id.in_(furniture_ids))
        )
        furnitures = {f.id: f for f in result.scalars().all()}

        missing = furniture_ids - set(furnitures.keys())
        if missing:
            raise HTTPException(
                status_code=404,
                detail=f"Furniture not found: {sorted(missing)}",
            )

        order_items: list[OrderItem] = []
        total_price = 0.0

        for item in data.items:
            furniture = furnitures[item.furniture_id]
            unit_price = float(furniture.price)
            line_total = unit_price * item.quantity
            total_price += line_total

            order_items.append(
                OrderItem(
                    furniture_id=item.furniture_id,
                    quantity=item.quantity,
                    price=unit_price,
                )
            )

        order = Order(
            client_email=data.client_email,
            total_price=total_price,
            items=order_items,
        )

        db.add(order)
        await db.commit()
        await db.refresh(order)

        return order

order_crud = OrderCRUD(Order)