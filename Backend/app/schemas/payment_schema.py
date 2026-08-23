from datetime import datetime

from pydantic import BaseModel


class PaymentCreate(BaseModel):

    booking_id: int

    payment_method: str


class PaymentUpdate(BaseModel):

    payment_status: str

    transaction_id: str


class PaymentResponse(BaseModel):

    id: int

    user_id: int

    booking_id: int

    amount: float

    payment_method: str

    payment_status: str

    transaction_id: str | None = None

    payment_date: datetime

    class Config:

        from_attributes = True