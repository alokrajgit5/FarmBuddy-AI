from datetime import date

from pydantic import BaseModel


class EquipmentBookingCreate(BaseModel):

    equipment_id: int

    start_date: date

    end_date: date


class EquipmentBookingUpdate(BaseModel):

    status: str


class EquipmentBookingResponse(BaseModel):

    id: int

    equipment_id: int

    renter_id: int

    start_date: date

    end_date: date

    total_days: int

    total_amount: float

    status: str

    class Config:

        from_attributes = True