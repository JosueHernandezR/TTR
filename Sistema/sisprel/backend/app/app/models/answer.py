import datetime
from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Column, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import Question  # noqa: F401
    from .user import User

class Answer(Base):
    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Integer(), nullable= False)
    open_answer = Column(Text, nullable=True)
    answered_at=Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    option_id = Column(Integer, nullable=True)
    question_id = Column(Integer, ForeignKey("question.id"), nullable=False)
    surveyed_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    # Relacion muchos a uno
    users = relationship("User", back_populates="answers")
    questions = relationship("Question", back_populates="answers")
