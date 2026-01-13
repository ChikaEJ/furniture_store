from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base_crud import BaseCRUD
from app.models.order import Order
from app.schemas.order import OrderRead


class OrderCRUD(BaseCRUD):
    async def get_orders_by_email(self, email: str, db: AsyncSession) -> List[OrderRead]:
        try:
            db_obj = await db.execute(
                select(self.model).where(self.model.client_email == email).order_by(self.model.id)
            )
            return db_obj.scalar().all()
        except Exception as e:
            await db.rollback()
            raise e

order_crud = OrderCRUD(Order)