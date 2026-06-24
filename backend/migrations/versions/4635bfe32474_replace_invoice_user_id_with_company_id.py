"""replace invoice user id with company id

Revision ID: 4635bfe32474
Revises: bf6b69a23583
Create Date: 2026-06-24 14:32:47.836522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4635bfe32474'
down_revision: Union[str, Sequence[str], None] = 'bf6b69a23583'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'invoices',
        sa.Column('company_id', sa.Integer(), nullable=True)
    )

    op.execute("""
        UPDATE invoices
        SET company_id = 1
        WHERE company_id IS NULL
    """)

    op.alter_column(
        'invoices',
        'company_id',
        nullable=False
    )

    op.drop_constraint(
        op.f('invoices_user_id_fkey'),
        'invoices',
        type_='foreignkey'
    )

    op.create_foreign_key(
        'invoices_company_id_fkey',
        'invoices',
        'companies',
        ['company_id'],
        ['id']
    )

    op.drop_column('invoices', 'user_id')


def downgrade() -> None:
    op.add_column(
        'invoices',
        sa.Column('user_id', sa.Integer(), nullable=True)
    )

    op.execute("""
        UPDATE invoices
        SET user_id = 2
        WHERE user_id IS NULL
    """)

    op.alter_column(
        'invoices',
        'user_id',
        nullable=False
    )

    op.drop_constraint(
        'invoices_company_id_fkey',
        'invoices',
        type_='foreignkey'
    )

    op.create_foreign_key(
        op.f('invoices_user_id_fkey'),
        'invoices',
        'users',
        ['user_id'],
        ['id']
    )

    op.drop_column('invoices', 'company_id')