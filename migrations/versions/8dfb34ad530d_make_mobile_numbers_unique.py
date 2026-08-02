"""Make mobile numbers unique

Revision ID: 8dfb34ad530d
Revises: 
Create Date: 2026-08-03 00:53:21.304659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dfb34ad530d'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.create_unique_constraint(
            "uq_user_mobile_number",
            ["mobile_number"]
        )


def downgrade():
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_constraint(
            "uq_user_mobile_number",
            type_="unique"
        )