from typing import TYPE_CHECKING
from sqlalchemy.sql.expression import null

from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from app.db.base_class import Base
from sqlalchemy import Column, Text, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import Question  # noqa: F401

class Question_option(Base):
    __mapper_args__ = {'polymorphic_identity': 'question_option'}
    
    id = Column(Integer, primary_key=True, nullable= False, index=True, unique=True, autoincrement=True)
    option_name = Column(String(3), nullable=False)
    option = Column(Text, nullable=False)
    weight = Column(Integer(), nullable=False)

    question_id = Column(Integer, ForeignKey("question.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True, index=True)

    question_survey_id = Column(Integer, ForeignKey("question.survey_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True, index=True)
