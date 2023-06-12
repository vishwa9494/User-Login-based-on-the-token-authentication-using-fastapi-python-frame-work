"""create posts table

Revision ID: e0b45293093b
Revises: 
Create Date: 2023-05-19 22:06:46.844585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0b45293093b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('vishwa',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('vishwa')
    pass
