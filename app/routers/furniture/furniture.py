from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.furniture import FurnitureRead
from app.crud.furniture import furniture_crud

router = APIRouter(prefix="/furniture", tags=["furniture"])

@router.get("/", response_model=List[FurnitureRead])
async def get_furniture(db: AsyncSession = Depends(get_db)) -> List[FurnitureRead]:
    return await furniture_crud.get_all(db=db)


@router.get("/{id}", response_model=FurnitureRead)
async def get_furniture_by_id(id: int, db: AsyncSession = Depends(get_db)) -> FurnitureRead:
    furniture = await furniture_crud.get(db, id)
    return FurnitureRead.model_validate(furniture)