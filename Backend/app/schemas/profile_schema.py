from pydantic import BaseModel


class ProfileCreate(BaseModel):

    phone: str

    state: str

    district: str

    village: str

    land_area: float

    soil_type: str

    main_crop: str

    irrigation: str

    experience: str

    bio: str

    profile_image: str


class ProfileResponse(BaseModel):

    id: int

    user_id: int

    phone: str

    state: str

    district: str

    village: str

    land_area: float

    soil_type: str

    main_crop: str

    irrigation: str

    experience: str

    bio: str

    profile_image: str

    class Config:
        from_attributes = True