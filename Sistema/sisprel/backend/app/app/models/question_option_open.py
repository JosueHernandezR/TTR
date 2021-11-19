from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Column, Text, ForeignKey, ForeignKeyConstraint, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import  Question

class Question_option_open(Base):
    id = Column(Integer, primary_key=True, index=True)
    weight_max = Column(Integer, nullable=False)

    question_id = Column(Integer, nullable=False)
    question_survey_id = Column(Integer, nullable=False)
    
    __table_args__ = (ForeignKeyConstraint(["question_id", "question_survey_id"],["question.id", "question.survey_id"]), {})
    # Relacion Muchos a 1
    questions = relationship("Question", back_populates="question_option_open")