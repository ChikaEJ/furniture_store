from typing import List, Dict, Any

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.exeptions import UserAlreadyExists, DatabaseUnavailable
from app.schemas.user import UserRead, UserCreate
from app.crud.user import user_crud

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=List[UserRead])
async def get_all_users(db: AsyncSession = Depends(get_db)) -> Sequence[UserRead]:
    users = await user_crud.get_all(db)
    if not users:
        raise HTTPException(status_code=404, detail="Something went wrong")
    return users

@router.post("/", response_model=UserRead)
async def create_user_rout(user: UserCreate, db: AsyncSession = Depends(get_db)) -> UserRead:
    """
    This is route to create a new user
    :param email:
    :return user:
    """
    try:
        db_user = await user_crud.create(user, db)
        return UserRead.model_validate(db_user)

    except UserAlreadyExists:
        raise HTTPException(
            status_code=409,
            detail=UserAlreadyExists.message
        )
    except DatabaseUnavailable:
        raise HTTPException(
            status_code=503,
            detail=DatabaseUnavailable.message
        )

@router.get("/{user_id}", response_model=UserRead)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)) -> UserRead:
    user = await user_crud.get(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserRead.model_validate(user)