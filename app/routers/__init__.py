from fastapi import APIRouter

from app.routers.weather import weather_api as weather
from app.routers.user import user

router = APIRouter()
router.include_router(user.router)
router.include_router(weather.router)