from pydantic import BaseModel


class FertilizerRequest(BaseModel):
    crop: str
    nitrogen: float
    phosphorus: float
    potassium: float


class FertilizerResponse(BaseModel):
    fertilizer: str
    quantity: str
    application_method: str
    instructions: str