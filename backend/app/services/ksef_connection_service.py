from app.models.ksef_connection import KsefConnection

from app.services.encryption_service import (
    encrypt_value,
    decrypt_value
)

def create_ksef_connection(
    db,
    company_id: int,
    token: str
):
    encrypted_token = encrypt_value(token)

    connection = KsefConnection(
        company_id=company_id,
        token=encrypted_token
    )

    db.add(connection)
    db.commit()
    db.refresh(connection)

    return connection

def get_ksef_connection(
    db,
    connection_id: int
):
    return (
        db.query(KsefConnection)
        .filter(KsefConnection.id == connection_id)
        .first()
    )
    
def get_active_ksef_connection(
    db,
    company_id: int
):
    connection = (
        db.query(KsefConnection)
        .filter(KsefConnection.company_id == company_id)
        .filter(KsefConnection.is_active == True)
        .first()
    )

    if not connection:
        return None

    connection.token = decrypt_value(
        connection.token
    )

    return connection