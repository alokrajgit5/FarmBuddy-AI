from pydantic import BaseModel
from typing import Optional


class TractorCreate(BaseModel):
    tractor_name: str
    brand: str
    model: str
    rent_per_day: float
    location: str
    owner_name: str
    owner_phone: str
    description: Optional[str] = None


class TractorResponse(BaseModel):
    id: int
    tractor_name: str
    brand: str
    model: str
    rent_per_day: float
    location: str
    owner_name: str
    owner_phone: str
    description: Optional[str]

    class Config:
        from_attributes = True