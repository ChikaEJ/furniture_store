from fastapi import APIRouter, HTTPException

from app.services.get_weather_api import get_weather_api

router = APIRouter(prefix="/weather", tags=["weather"])

@router.get("/")
async def get_weather():
    try:
        result = await get_weather_api()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))