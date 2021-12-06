"""Tercera version estable

Revision ID: dce6a7a2ef32
Revises: 066d652dab8a
Create Date: 2021-12-06 05:44:28.641463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dce6a7a2ef32'
down_revision = '066d652dab8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prediction_manual', sa.Column('iteraciones_para_eliminación', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('prediction_manual', 'iteraciones_para_eliminación')
    # ### end Alembic commands ###