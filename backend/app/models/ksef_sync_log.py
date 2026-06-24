from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.user import Base


class KsefSyncLog(Base):
    __tablename__ = "ksef_sync_logs"

    id: Mapped[int] = mapped_column(primary_key=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False
    )

    status: Mapped[str]

    invoices_found: Mapped[int] = mapped_column(
        default=0
    )

    error_message: Mapped[str | None] = mapped_column(
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )