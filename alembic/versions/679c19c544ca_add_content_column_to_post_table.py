"""add content column to post table

Revision ID: 679c19c544ca
Revises: d717b4482c50
Create Date: 2024-06-05 14:51:16.203830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '679c19c544ca'
down_revision: Union[str, None] = 'd717b4482c50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
