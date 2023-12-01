"""Drop ix_user_email

Revision ID: 55fddd383fe5
Revises: bb4c19ccf72b
Create Date: 2023-12-01 07:34:57.730656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55fddd383fe5'
down_revision: Union[str, None] = 'bb4c19ccf72b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index('ix_user_email', table_name='user')


def downgrade() -> None:
    pass
