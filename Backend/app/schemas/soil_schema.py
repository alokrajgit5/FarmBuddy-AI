from pydantic import BaseModel


class SoilCreate(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    ph: float
    moisture: float


class SoilResponse(SoilCreate):
    id: int

    class Config:
        from_attributes = True


class SoilRecommendation(BaseModel):
    recommendation: str