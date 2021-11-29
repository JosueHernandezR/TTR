from typing import TYPE_CHECKING

from sqlalchemy.sql.schema import PrimaryKeyConstraint
from app.db.base_class import Base
from sqlalchemy import Column, ForeignKeyConstraint, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import  Question

class Question_option_open(Base):
    id = Column(Integer, index=True, unique=True)
    weight_max = Column(Integer, nullable=False)

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
    
    #__table_args__ = (ForeignKeyConstraint(["question_id", "question_survey_id"],["question.id", "question.survey_id"]), {})
    # Relacion Muchos a 1
    questions = relationship("Question", back_populates="question_option_open")
    answers = relationship("Answer_Option_Open", back_populates="question_option_open_answer")