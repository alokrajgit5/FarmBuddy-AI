from datetime import datetime

from pydantic import BaseModel, Field


class EquipmentReviewCreate(BaseModel):

    equipment_id: int

    rating: int = Field(
        ge=1,
        le=5
    )

    review: str


class EquipmentReviewUpdate(BaseModel):

    rating: int = Field(
        ge=1,
        le=5
    )

    review: str


class EquipmentReviewResponse(BaseModel):

    id: int

    equipment_id: int

    reviewer_id: int

    rating: int

    review: str

    created_at: datetime

    class Config:

        from_attributes = True