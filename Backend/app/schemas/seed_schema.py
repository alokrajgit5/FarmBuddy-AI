from pydantic import BaseModel


class SeedCreate(BaseModel):

    seed_name: str

    crop_name: str

    variety: str

    quantity: float

    unit: str

    price: float

    description: str

    image: str


class SeedUpdate(BaseModel):

    seed_name: str

    crop_name: str

    variety: str

    quantity: float

    unit: str

    price: float

    description: str

    image: str


class SeedResponse(BaseModel):

    id: int

    seller_id: int

    seed_name: str

    crop_name: str

    variety: str

    quantity: float

    unit: str

    price: float

    description: str

    image: str

    class Config:
        from_attributes = True