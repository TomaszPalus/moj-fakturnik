from app.core.database import SessionLocal

from app.services.ksef_connection_service import (
    get_active_ksef_connection
)

db = SessionLocal()

connection = get_active_ksef_connection(
    db=db,
    company_id=1
)

print(connection.token)