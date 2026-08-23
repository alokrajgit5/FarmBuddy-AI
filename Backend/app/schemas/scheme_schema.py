from pydantic import BaseModel


class SchemeRequest(BaseModel):
    state: str
    land_size: float
    crop: str


class SchemeItem(BaseModel):
    scheme_name: str
    eligibility: str
    eligibility_reason: str
    benefit: str
    subsidy: str
    application_mode: str
    documents_required: list[str]
    official_portal: str
    approval_time: str
    last_date: str
    important_note: str


class SchemeResponse(BaseModel):
    recommendations: list[SchemeItem]