"""Renaming user table to users

Revision ID: bb4c19ccf72b
Revises: fcf516f9954a
Create Date: 2023-11-28 08:05:17.009004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb4c19ccf72b'
down_revision: Union[str, None] = 'fcf516f9954a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('user', 'users')


def downgrade() -> None:
    op.rename_table('users', 'user')
