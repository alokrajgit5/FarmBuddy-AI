from pydantic import BaseModel


class LaborBookingCreate(BaseModel):

    labor_id: int

    booking_date: str

    working_days: int


class LaborBookingResponse(BaseModel):

    id: int

    farmer_id: int

    labor_id: int

    booking_date: str

    working_days: int

    total_amount: float

    status: str

    class Config:
        from_attributes = True


class LaborBookingUpdate(BaseModel):

    status: str