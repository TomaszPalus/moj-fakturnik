from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    nip: str