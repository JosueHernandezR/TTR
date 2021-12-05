from typing import TYPE_CHECKING

from sqlalchemy.sql.schema import PrimaryKeyConstraint
from app.db.base_class import Base
from sqlalchemy import Column, ForeignKey,ForeignKeyConstraint, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import  Question

class Question_option_open(Base):
    id = Column(Integer, index=True, unique=True)
    weight_max = Column(Integer, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True, index=True)
    question_survey_id = Column(Integer, ForeignKey("question.survey_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True, index=True)
