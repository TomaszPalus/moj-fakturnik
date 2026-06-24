from pydantic import BaseModel


class KsefConnectionCreate(BaseModel):
    company_id: int
    token: str