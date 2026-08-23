from pydantic import BaseModel


class EquipmentCreate(BaseModel):

    equipment_name: str

    category: str

    brand: str

    model: str

    price_per_day: float

    location: str

    description: str

    image: str


class EquipmentUpdate(BaseModel):

    equipment_name: str

    category: str

    brand: str

    model: str

    price_per_day: float

    location: str

    description: str

    image: str

    availability: str


class EquipmentResponse(BaseModel):

    id: int

    owner_id: int

    equipment_name: str

    category: str

    brand: str

    model: str

    price_per_day: float

    location: str

    description: str

    image: str

    availability: str

    class Config:

        from_attributes = True