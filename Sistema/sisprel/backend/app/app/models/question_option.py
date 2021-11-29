from typing import TYPE_CHECKING

from sqlalchemy.sql.schema import PrimaryKeyConstraint, UniqueConstraint
from app.db.base_class import Base
from sqlalchemy import Column, Text, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import Question  # noqa: F401

class Question_option(Base):
    id = Column(Integer, index=True, unique=True)
    option_name = Column(String(3), nullable=False)
    option = Column(Text, nullable=False)
    weight = Column(Integer(), nullable=False)

    question_id = Column(Integer,nullable=False, unique=True)
    question_survey_id = Column(Integer,nullable=False, unique=True)
    
    __table_args__ = (
        ForeignKeyConstraint(
            ["question_id", "question_survey_id"],
            ["question.id", "question.survey_id"], 
            onupdate="CASCADE", ondelete="CASCADE",
        ),
        PrimaryKeyConstraint("id", "question_id", "question_survey_id"),
        UniqueConstraint("id", "question_id", "question_survey_id"),
    )
    #__table_args__ = 
    # Relacion Muchos a 1
    questions = relationship("Question", back_populates="question_options")
    answers = relationship("Answer_Option", back_populates="question_options_answer")
