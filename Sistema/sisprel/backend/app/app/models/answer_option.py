from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User # noqa: F401
    from .question_option import Question_option # noqa: F401

class Answer_Option(Base):
    #User id
    respondent_id = Column(ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True)
    #Question option FK
    option_id = Column(ForeignKey("question_option.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)
    option_question_id = Column(ForeignKey("question_option.question_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)
    option_question_survey_id = Column(ForeignKey("question_option.question_survey_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)
    
    weight_elected = Column(Integer, nullable=False)

    __table_args__ = (
            UniqueConstraint("respondent_id", "option_id", "option_question_id", "option_question_survey_id",),
        )

    respondents = relationship("User", back_populates="answer_options")
    question_options_answer = relationship("Question_option", back_populates="answers")