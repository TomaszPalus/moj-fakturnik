from app.services.ksef_sync_log_service import (
    create_sync_log
)

from app.models.company import Company
from app.models.invoice import Invoice

from app.services.invoice_service import invoice_exists
from app.services.notification_service import (
    get_active_user_channels
)

from app.services.telegram_service import (
    send_telegram_message
)
from app.services.ksef_connection_service import (
    get_active_ksef_connection
)
from app.services.ksef_client import (
    test_connection
)

def run_mock_sync(
    db,
    company_id: int
):
    connection = get_active_ksef_connection(
        db=db,
        company_id=company_id
    )
    if not connection:
        return create_sync_log(
            db=db,
            company_id=company_id,
            status="FAILED",
            invoices_found=0,
            error_message="No active KSeF connection found."
        )
        
    result = test_connection(
        token=connection.token
    )
    if not result["success"]:
        return create_sync_log(
            db=db,
            company_id=company_id,
            status="FAILED",
            invoices_found=0,
            error_message=result["message"]
        )
    new_invoices_count=0
    
    for i in range(1, 4):
        invoice_number = f"KSEF/2026/{i:03d}"

        if invoice_exists(
            db=db,
            company_id=company_id,
            invoice_number=invoice_number
        ):
            continue

        invoice = Invoice(
            company_id=company_id,
            invoice_number=invoice_number,
            seller_name="KSeF Mock Supplier",
            amount=1000.0 * i
        )

        db.add(invoice)
        new_invoices_count += 1

    db.commit()
    
    log = create_sync_log(
        db=db,
        company_id=company_id,
        status="SUCCESS",
        invoices_found=new_invoices_count
    )

    company = (
        db.query(Company)
        .filter(Company.id == company_id)
        .first()
    )

    if company:

        channels = get_active_user_channels(
            db=db,
            user_id=company.owner_user_id
        )

        for channel in channels:

            if channel.type == "telegram":

                send_telegram_message(
                    chat_id=channel.destination,
                    text=(
                        f"🔄 Synchronizacja KSeF zakończona\n\n"
                        f"Firma ID: {company_id}\n"
                        f"Nowe faktury: {new_invoices_count}\n"
                        f"Status: SUCCESS"
                    )
                )

    return log