from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    ph: float
    moisture: float
    temperature: float
    humidity: float


class CropRecommendation(BaseModel):
    crop: str
    confidence: int
    season: str
    fertilizer: str


class RecommendationResponse(BaseModel):
    recommendations: list[CropRecommendation]