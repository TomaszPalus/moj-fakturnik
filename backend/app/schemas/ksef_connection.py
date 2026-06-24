from datetime import datetime

from pydantic import BaseModel


class KsefConnectionCreate(BaseModel):
    company_id: int
    token: str


class KsefConnectionResponse(BaseModel):
    id: int
    company_id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True