from datetime import date

from pydantic import BaseModel


class TractorBookingCreate(BaseModel):

    tractor_id: int

    booking_date: date

    total_days: int

    message: str | None = None


class TractorBookingResponse(BaseModel):

    id: int

    tractor_id: int

    farmer_id: int

    booking_date: date

    total_days: int

    message: str | None = None

    status: str

    class Config:
        from_attributes = True