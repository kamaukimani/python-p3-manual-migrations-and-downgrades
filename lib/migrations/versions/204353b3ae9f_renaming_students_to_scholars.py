"""Renaming students to scholars

Revision ID: 204353b3ae9f
Revises: 791279dd0760
Create Date: 2025-08-25 04:06:53.763435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '204353b3ae9f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
