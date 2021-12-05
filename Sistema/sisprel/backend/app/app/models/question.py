from typing import TYPE_CHECKING
from uuid import uuid4
from sqlalchemy.sql.expression import true

from sqlalchemy.sql.schema import ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, Text, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .survey import Survey  # noqa: F401

class Question(Base):
    __mapper_args__ = {'polymorphic_identity': 'question'}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question = Column(Text,index=True, nullable=False)
    accept_open_answer = Column(Boolean(), nullable=False)
    is_mandatory = Column(Boolean(), default=True, nullable=False)
    
    survey_id = Column(Integer, ForeignKey("survey.id", onupdate="CASCADE", ondelete="CASCADE"),primary_key=True, unique=True, index=True)

    survey = relationship(
        "Survey", 
        foreign_keys='Question.survey_id',
        backref= 'question',
        primaryjoin="and_(Question.id == Question_option.question_id, Question.survey_id == Question_option.question_survey_id)",

    )

    __table_args__ = (
        UniqueConstraint("id", "survey_id",),
        PrimaryKeyConstraint("id", "survey_id",),
    )
    # Relacion 1 a muchos
    #question_options = relationship("Question_option", back_populates="questions")
    # Relacion 1 a 1
    question_option_open =relationship("Question_option_open", back_populates="questions", uselist=False)
    #__table_args__ = (UniqueConstraint("id", "survey_id", name="uq_question_survey_unique_code"),)
    # Relacion muchos a 1
    #surveys = relationship("Survey", back_populates="questions")
