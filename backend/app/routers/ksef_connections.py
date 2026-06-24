from fastapi import APIRouter
from fastapi import Depends

from app.dependencies import get_db
from app.dependencies import get_current_user

from app.schemas.ksef_connection import (
    KsefConnectionCreate
)

from app.services.ksef_connection_service import (
    create_ksef_connection,
    get_ksef_connections
)

router = APIRouter(
    prefix="/ksef-connections",
    tags=["ksef-connections"]
)


@router.post("")
def add_ksef_connection(
    data: KsefConnectionCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_ksef_connection(
        db=db,
        company_id=data.company_id,
        token=data.token
    )
    
@router.get("")
def list_ksef_connections(
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_ksef_connections(db=db)