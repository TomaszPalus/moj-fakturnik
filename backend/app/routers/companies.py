from fastapi import APIRouter
from fastapi import Depends

from app.dependencies import get_db
from app.dependencies import get_current_user

from app.schemas.company import CompanyCreate

from app.services.company_service import (
    create_company,
    get_user_companies
)

router = APIRouter(
    prefix="/companies",
    tags=["companies"]
)


@router.post("")
def add_company(
    data: CompanyCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_company(
        db=db,
        owner_user_id=current_user.id,
        name=data.name,
        nip=data.nip
    )
    
@router.get("")
def list_companies(
    db=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_user_companies(
        db=db,
        owner_user_id=current_user.id
    )