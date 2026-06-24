from pydantic import BaseModel


class InvoiceCreate(BaseModel):
    invoice_number: str
    seller_name: str
    amount: float