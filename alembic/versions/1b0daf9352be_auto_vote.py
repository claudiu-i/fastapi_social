"""auto-vote

Revision ID: 1b0daf9352be
Revises: 3bee687eb027
Create Date: 2024-06-05 15:18:54.850144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b0daf9352be'
down_revision: Union[str, None] = '3bee687eb027'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='Cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='Cascade'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    op.drop_column('users', 'passwword')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('passwword', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'password')
    op.drop_column('posts', 'content')
    op.drop_table('votes')
    # ### end Alembic commands ###