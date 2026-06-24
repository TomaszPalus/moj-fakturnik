from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.user import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    invoice_number: Mapped[str]

    seller_name: Mapped[str]

    amount: Mapped[float]

    issue_date: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )