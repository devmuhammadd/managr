"""create users table

Revision ID: fcf516f9954a
Revises: e7167fb40a48
Create Date: 2023-11-25 08:45:26.999574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcf516f9954a'
down_revision: Union[str, None] = 'e7167fb40a48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('email', sa.String, nullable=False, unique=True, index=True),
        sa.Column('username', sa.String, nullable=False, unique=True, index=True),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('is_superuser', sa.Boolean, default=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('full_name', sa.String, nullable=False),
    )

def downgrade():
    op.drop_table('user')