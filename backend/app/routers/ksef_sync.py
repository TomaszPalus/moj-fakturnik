from fastapi import APIRouter
from fastapi import Depends

from app.core.dependencies import get_db
from app.core.dependencies import get_current_user

from app.services.ksef_sync_service import (
    run_mock_sync
)
from app.services.ksef_sync_log_service import (
    get_company_sync_logs
)
from app.services.company_service import (
    get_company_or_404
)

router = APIRouter(
    prefix="/companies/{company_id}/ksef-sync",
    tags=["ksef-sync"]
)


@router.post("")
def sync_company(
    company_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    get_company_or_404(
        db=db,
        company_id=company_id,
        owner_user_id=current_user.id
    )
    return run_mock_sync(
        db=db,
        company_id=company_id
    )

@router.get("/logs")
def list_sync_logs(
    company_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    get_company_or_404(
        db=db,
        company_id=company_id,
        owner_user_id=current_user.id
    )
    return get_company_sync_logs(
        db=db,
        company_id=company_id
    )