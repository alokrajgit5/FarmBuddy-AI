from pydantic import BaseModel


class CropCreate(BaseModel):
    crop_name: str
    season: str
    area: float
    irrigation: str
    fertilizer: str
    expected_yield: float


class CropResponse(BaseModel):
    id: int
    crop_name: str
    season: str
    area: float
    irrigation: str
    fertilizer: str
    expected_yield: float

    class Config:
        from_attributes = True