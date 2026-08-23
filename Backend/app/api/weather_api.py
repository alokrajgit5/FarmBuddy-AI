from fastapi import APIRouter, HTTPException

from app.schemas.weather_schema import WeatherResponse
from app.services.weather_service import get_weather

router = APIRouter(
    prefix="/api/weather",
    tags=["Weather"]
)


@router.get(
    "/{city}",
    response_model=WeatherResponse
)
def weather(city: str):

    data = get_weather(city)

    if not data:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    return data