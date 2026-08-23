from pydantic import BaseModel


class CropRecommendationRequest(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float


class CropItem(BaseModel):
    crop: str
    suitability: str
    duration: str
    expected_yield: str
    advantages: list[str]


class CropRecommendationResponse(BaseModel):
    recommendations: list[CropItem]