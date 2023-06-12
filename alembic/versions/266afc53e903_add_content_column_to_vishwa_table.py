"""add content column to vishwa table

Revision ID: 266afc53e903
Revises: d9fb08d099c3
Create Date: 2023-05-19 22:27:07.295597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '266afc53e903'
down_revision = 'd9fb08d099c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('vishwa',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('vishwa','content')
    pass
