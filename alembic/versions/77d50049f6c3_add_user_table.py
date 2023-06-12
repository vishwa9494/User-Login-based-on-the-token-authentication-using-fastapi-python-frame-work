"""add user table

Revision ID: 77d50049f6c3
Revises: 266afc53e903
Create Date: 2023-05-19 23:12:48.658176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77d50049f6c3'
down_revision = '266afc53e903'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('user',sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('user')
    pass
