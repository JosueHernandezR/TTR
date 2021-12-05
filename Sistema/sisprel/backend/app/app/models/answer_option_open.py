from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User # noqa: F401
    from .question_option import Question_option # noqa: F401

class Answer_Option_Open(Base):
    #User id
    respondent_id = Column(ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True)
    #Question option FK
    option_id = Column(ForeignKey("question_option.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)
    option_question_id = Column(ForeignKey("question_option.question_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)
    option_question_survey_id = Column(ForeignKey("question_option.question_survey_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)

    answer_text = Column(Text, nullable=False)
    weight_calculated = Column(Integer, nullable=False)

   