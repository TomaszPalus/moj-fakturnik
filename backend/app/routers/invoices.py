from fastapi import APIRouter
from fastapi import Depends

from app.dependencies import get_db
from app.dependencies import get_current_user

from app.schemas.invoice import InvoiceCreate

from app.services.invoice_service import create_invoice

router = APIRouter(
    prefix="/invoices",
    tags=["invoices"]
)


@router.post("/mock")
def add_mock_invoice(
    data: InvoiceCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_invoice(
        db=db,
        user_id=current_user.id,
        invoice_number=data.invoice_number,
        seller_name=data.seller_name,
        amount=data.amount
    )