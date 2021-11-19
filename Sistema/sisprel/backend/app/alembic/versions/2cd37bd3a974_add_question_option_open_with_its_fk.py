"""Add question option open with its FK

Revision ID: 2cd37bd3a974
Revises: 86d6c4fdc25b
Create Date: 2021-11-18 06:36:10.721514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cd37bd3a974'
down_revision = '86d6c4fdc25b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question_option_open',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weigth_max', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question_survey_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id', 'question_survey_id'], ['question.id', 'question.survey_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_option_open_id'), 'question_option_open', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_question_option_open_id'), table_name='question_option_open')
    op.drop_table('question_option_open')
    # ### end Alembic commands ###