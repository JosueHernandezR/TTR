"""Add weight total at survey

Revision ID: 3e12bc3e8aec
Revises: dce6a7a2ef32
Create Date: 2021-12-06 08:16:17.943265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e12bc3e8aec'
down_revision = 'dce6a7a2ef32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey', sa.Column('weight_total', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('survey', 'weight_total')
    # ### end Alembic commands ###