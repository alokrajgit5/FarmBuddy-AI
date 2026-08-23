from pydantic import BaseModel
from typing import Optional


class LaborBase(BaseModel):
    worker_name: str
    phone: str
    village: str
    work_type: str
    experience: int
    daily_wage: float
    available: bool = True


class LaborCreate(LaborBase):
    pass


class LaborUpdate(BaseModel):
    worker_name: Optional[str] = None
    phone: Optional[str] = None
    village: Optional[str] = None
    work_type: Optional[str] = None
    experience: Optional[int] = None
    daily_wage: Optional[float] = None
    available: Optional[bool] = None


class LaborResponse(LaborBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True