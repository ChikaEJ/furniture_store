
from fastapi import HTTPException
from sqlalchemy import select
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
                selectinload(Order.items)
                .selectinload(OrderItem.furniture)
            )
            .order_by(Order.id)
        )

        orders = result.scalars().all()

        return [
            OrderRead(
                id=order.id,
                client_email=order.client_email,
                total_price=order.total_price,
                items=order.items
            )
            for order in orders
        ]

    async def create_order(
            self,
            data: OrderCreate,
            db: AsyncSession,
    ) -> Order:

        furniture_ids = [item.furniture_id for item in data.items]

        result = await db.execute(
            select(Furniture)
            .where(Furniture.id.in_(furniture_ids))
        )
        furnitures = result.scalars().all()

        if len(furnitures) != len(furniture_ids):
            raise HTTPException(
                status_code=400,
                detail="Some furniture items not found"
            )

        furniture_map = {f.id: f for f in furnitures}

        order = Order(
            client_email=data.client_email,
            total_price=0,
        )
        db.add(order)
        await db.flush()

        total_price = 0
        order_items: list[OrderItem] = []

        for item in data.items:
            furniture = furniture_map[item.furniture_id]
            item_price = furniture.price * item.quantity
            total_price += item_price

            order_item = OrderItem(
                order_id=order.id,
                furniture_id=furniture.id,
                quantity=item.quantity,
                price=furniture.price,
            )
            order_items.append(order_item)

        db.add_all(order_items)

        order.total_price = total_price

        await db.commit()

        result = await db.execute(
            select(Order)
            .where(Order.id == order.id)
            .options(
                selectinload(Order.items)
                .selectinload(OrderItem.furniture)
            )
        )
        return result.scalar_one()
order_crud = OrderCRUD(Order)