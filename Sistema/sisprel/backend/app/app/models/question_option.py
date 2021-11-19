from typing import TYPE_CHECKING
from app.db.base_class import Base
from sqlalchemy import Column, Text, ForeignKey, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import Question  # noqa: F401

class Question_option(Base):
    id = Column(Integer, primary_key=True, index=True)
    option_name = Column(String(3), nullable=False)
    option = Column(Text, nullable=False)
    weight = Column(Integer(), nullable=False)

    question_id = Column(Integer, nullable=False)
    question_survey_id = Column(Integer, nullable=False)
    
    __table_args__ = (ForeignKeyConstraint(["question_id", "question_survey_id"],["question.id", "question.survey_id"]), {})
    # Relacion Muchos a 1
    questions = relationship("Question", back_populates="question_options")