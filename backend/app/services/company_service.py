from app.models.company import Company


def create_company(
    db,
    owner_user_id: int,
    name: str,
    nip: str
):
    company = Company(
        owner_user_id=owner_user_id,
        name=name,
        nip=nip
    )

    db.add(company)
    db.commit()
    db.refresh(company)

    return company

def get_user_companies(
    db,
    owner_user_id: int
):
    return (
        db.query(Company)
        .filter(Company.owner_user_id == owner_user_id)
        .order_by(Company.id.desc())
        .all()
    )