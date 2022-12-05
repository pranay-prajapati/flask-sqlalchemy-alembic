"""Added address

Revision ID: 0002
Revises: 0001
Create Date: 2022-08-01 19:12:50.357338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade():
    try:
        op.add_column('users', sa.Column('address', sa.String(length=120)))
    except Exception as e:
        # To handle when alembic table got deleted
        pass


def downgrade():
    op.drop_column('users', 'address')
