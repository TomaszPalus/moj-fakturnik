from app.models.ksef_sync_log import KsefSyncLog


def create_sync_log(
    db,
    company_id: int,
    status: str,
    invoices_found: int = 0,
    error_message: str | None = None
):
    log = KsefSyncLog(
        company_id=company_id,
        status=status,
        invoices_found=invoices_found,
        error_message=error_message
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log

def get_company_sync_logs(
    db,
    company_id: int
):
    return (
        db.query(KsefSyncLog)
        .filter(KsefSyncLog.company_id == company_id)
        .order_by(KsefSyncLog.id.desc())
        .all()
    )