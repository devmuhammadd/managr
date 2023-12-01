"""Drop user indexes


Revision ID: bf9b4b66eb93
Revises: 55fddd383fe5
Create Date: 2023-12-01 07:36:28.068392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf9b4b66eb93'
down_revision: Union[str, None] = '55fddd383fe5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index('ix_user_id', table_name='user')
    op.drop_index('ix_user_username', table_name='user')


def downgrade() -> None:
    pass
