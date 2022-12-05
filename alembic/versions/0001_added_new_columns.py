"""Added new columns

Revision ID: 0001
Revises: 
Create Date: 2022-08-01 18:45:50.416978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    try:
        op.add_column('users', sa.Column('contact_number', sa.String(length=10)))
    except Exception as e:
        # To handle when alembic table got deleted
        pass


def downgrade():
    op.drop_column('users', 'contact_number')
