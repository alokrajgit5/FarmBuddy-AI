from pydantic import BaseModel


class SeedPurchaseCreate(BaseModel):

    seed_id: int

    quantity: float

    purchase_date: str


class SeedPurchaseUpdate(BaseModel):

    status: str


class SeedPurchaseResponse(BaseModel):

    id: int

    buyer_id: int

    seed_id: int

    quantity: float

    total_price: float

    purchase_date: str

    status: str

    class Config:
        from_attributes = True