from typing import TYPE_CHECKING
from sqlalchemy.sql.expression import null

from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from app.db.base_class import Base
from sqlalchemy import Column, Text, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import Question  # noqa: F401

class Question_option(Base):
    id = Column(Integer, nullable= False, index=True, autoincrement=True, primary_key=True)
    option_name = Column(String(3), nullable=False)
    option = Column(Text, nullable=False)
    weight = Column(Integer(), nullable=False)

    #question_id = Column(Integer, nullable=False, index=True, primary_key=True)
    question_id = Column(Integer, ForeignKey("question.id", onupdate="CASCADE", ondelete="CASCADE"))
    #"uestion_survey_id = Column(Integer, nullable=False, index=True, primary_key=True)
    #question_survey_id = Column(Integer, ForeignKey("question.survey_id"))
    question_survey_id = Column(Integer, nullable=False)
    question = relationship(
        "Question",
        foreign_keys=[question_id]
    )
    # question_survey = relationship(
    #     "Question",
    #     foreign_keys=[question_survey_id]
    # )

    # __table_args__ = (
    #     #ForeignKeyConstraint(["question_id", "question_survey_id"],["question.id", "question.survey_id"]),
    #     #PrimaryKeyConstraint("id", "question_id", "question_survey_id"),
    #     UniqueConstraint("id", "question_id","question_survey_id"),
    # )

    # Relacion Muchos a 1
    questions = relationship("Question", back_populates="question_options")
