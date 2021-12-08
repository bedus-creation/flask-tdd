"""create users table

Revision ID: 0ef514ba6771
Revises:
Create Date: 2020-07-16 13:01:24.395528

"""
from alembic import op
from bootstrap.app import db


# revision identifiers, used by Alembic.
revision = '0ef514ba6771'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        db.Column('id', db.Integer, primary_key=True),
        db.Column('fullname', db.String, nullable=False),
        db.Column('email', db.String, nullable=False),
        db.Column('password', db.String, nullable=False),
    )


def downgrade():
    op.drop_table('account')
