"""quit nullable at owner_id from Survey

Revision ID: 90d6d2351e54
Revises: 406303b6e85d
Create Date: 2021-10-30 06:19:57.414950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d6d2351e54'
down_revision = '406303b6e85d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('survey', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('survey', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###