from typing import Type, Dict, Any, TypeVar, Generic

from pydantic import BaseModel
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.sync import update

from app.core.database import Base
from app.core.exeptions import UserAlreadyExists

ModelType = TypeVar("ModelType", bound=Base)

class BaseCRUD(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    async def create(self, data: BaseModel, db: AsyncSession):
        obj = self.model(**data.model_dump())
        db.add(obj)
        try:
            await db.commit()
            await db.refresh(obj)
            return obj
        except Exception as e:
            await db.rollback()
            raise UserAlreadyExists()

    async def get(self, db: AsyncSession, odj_id: int):
        try:
            db_obj = await db.execute(
                select(self.model).where(self.model.id == odj_id)
            )
            return db_obj.scalar_one_or_none()
        except Exception as e:
            await db.rollback()
            raise e

    async def get_all(self, db: AsyncSession):
        try:
            db_objs = await db.execute(select(self.model).order_by(self.model.id))
            return db_objs.scalars().all()
        except Exception as e:
            await db.rollback()
            raise e

    async def update(self, db: AsyncSession, obj_id: int, data: Dict[str, Any]):
        try:
            db_obj = await db.execute(
                update(self.model).where(self.model.id == obj_id).values(**data)
            )
            await db.commit()
            await db.refresh(db_obj)
            return db_obj.scalar_one_or_none()
        except Exception as e:
            await db.rollback()
            raise e

    async def delete(self, db: AsyncSession, odj_id: int):
        try:
            db_obj = await db.execute(
                delete(self.model).where(self.model.id == odj_id)
            )
            await db.commit()
            return db_obj.scalar_one_or_none()
        except Exception as e:
            await db.rollback()
            raise e