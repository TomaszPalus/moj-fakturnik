from app.models.invoice import Invoice

from app.services.notification_service import (
    get_active_user_channels
)

from app.services.telegram_service import (
    send_telegram_message
)


def create_invoice(
    db,
    company_id: int,
    user_id: int,
    invoice_number: str,
    seller_name: str,
    amount: float
):
    invoice = Invoice(
        company_id=company_id,
        invoice_number=invoice_number,
        seller_name=seller_name,
        amount=amount
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    channels = get_active_user_channels(
        db=db,
        user_id=user_id
    )

    for channel in channels:

        if channel.type == "telegram":

            send_telegram_message(
                chat_id=channel.destination,
                text=(
                    f"📄 Nowa faktura\n\n"
                    f"Numer: {invoice_number}\n"
                    f"Sprzedawca: {seller_name}\n"
                    f"Kwota: {amount} PLN"
                )
            )

    return invoice

def get_company_invoices(
    db,
    company_id: int
):
    return (
        db.query(Invoice)
        .filter(Invoice.company_id == company_id)
        .order_by(Invoice.id.desc())
        .all()
    )
    
def invoice_exists(
    db,
    company_id: int,
    invoice_number: str
):
    return (
        db.query(Invoice)
        .filter(Invoice.company_id == company_id)
        .filter(Invoice.invoice_number == invoice_number)
        .first()
        is not None
    )