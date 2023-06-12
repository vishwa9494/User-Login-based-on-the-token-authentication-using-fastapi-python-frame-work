"""create vishwa table

Revision ID: 906c3f38f1fc
Revises: d46810e21682
Create Date: 2023-05-19 22:22:52.972522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '906c3f38f1fc'
down_revision = 'd46810e21682'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('vishwa',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('vishwa')
    pass

