from typing import Any

from pydantic import BaseModel, ConfigDict


class DashboardResponse(BaseModel):
    model_config = ConfigDict(
        extra="ignore"
    )

    # =========================================================
    # Farmer
    # =========================================================

    farmer_name: str
    current_date: str
    location: str
    verified: bool

    # =========================================================
    # Crops
    # =========================================================

    total_crops: int
    total_land: float
    active_crops: int

    # =========================================================
    # Weather
    # =========================================================

    weather_status: str
    temperature: float
    humidity: int
    wind_speed: float
    city: str
    updated_at: str

    weather: dict[str, Any]

    # =========================================================
    # Market / AI
    # =========================================================

    market_price: str
    ai_tip: str

    # =========================================================
    # Bookings
    # =========================================================

    total_bookings: int
    tractor_bookings: int
    labor_bookings: int
    seed_purchases: int
    bookings_this_month: int

    # =========================================================
    # Finance
    # =========================================================

    income: float
    expenses: float
    total_spending: float

    # =========================================================
    # Profile / Notifications
    # =========================================================

    profile_completion: int
    notification_count: int

    # =========================================================
    # Booking Graph
    # =========================================================

    monthly_booking_graph: list[Any]

    # =========================================================
    # Crop Health
    # =========================================================

    crop_health: int
    crop_health_score: int
    crop_health_status: str
    disease_risk: str
    crop_recommendation: str

    # =========================================================
    # AI Score
    # =========================================================

    ai_score: int

    # =========================================================
    # Activities
    # =========================================================

    recent_activities: list[Any]