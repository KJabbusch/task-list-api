"""creating Goal model

Revision ID: 59d325de6a7b
Revises: be1cb0c0f902
Create Date: 2021-10-29 10:24:42.974483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59d325de6a7b'
down_revision = 'be1cb0c0f902'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(length=100), nullable=False))
    op.drop_column('task', 'is_complete')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_complete', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###