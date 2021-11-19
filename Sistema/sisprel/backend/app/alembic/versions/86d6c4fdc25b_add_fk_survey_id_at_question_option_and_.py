"""Add FK Survey id at Question_option and Uniqueconstraint at question

Revision ID: 86d6c4fdc25b
Revises: e0d1f237081c
Create Date: 2021-11-18 04:36:35.295629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86d6c4fdc25b'
down_revision = 'e0d1f237081c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('Question_survey_unique_code', 'question', ['id', 'survey_id'])
    op.drop_constraint('question_option_question_id_fkey', 'question_option', type_='foreignkey')
    op.create_foreign_key(None, 'question_option', 'question', ['question_id', 'question_survey_id'], ['id', 'survey_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question_option', type_='foreignkey')
    op.create_foreign_key('question_option_question_id_fkey', 'question_option', 'question', ['question_id'], ['id'])
    op.drop_constraint('Question_survey_unique_code', 'question', type_='unique')
    # ### end Alembic commands ###