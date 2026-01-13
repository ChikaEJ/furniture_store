from fastapi import APIRouter
from app.routers.order.order import router as order_router
from app.routers.furniture.furniture import router as furniture_router
router = APIRouter()
router.include_router(order_router)
router.include_router(furniture_router)