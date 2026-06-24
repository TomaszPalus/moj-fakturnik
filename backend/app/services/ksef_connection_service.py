from app.models.ksef_connection import KsefConnection

def create_ksef_connection(
    db,
    company_id: int,
    token: str
):
    connection = KsefConnection(
        company_id=company_id,
        token=token
    )

    db.add(connection)
    db.commit()
    db.refresh(connection)

    return connection

def get_ksef_connections(
    db
):
    return (
        db.query(KsefConnection)
        .order_by(KsefConnection.id.desc())
        .all()
    )