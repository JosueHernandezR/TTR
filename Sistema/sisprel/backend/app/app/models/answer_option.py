from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, Text
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql.schema import ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint

from .question_option import Question_option

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User # noqa: F401
    from .question_option import Question_option # noqa: F401

class Answer_Option(Base):
    
    #User id
    respondent_id = Column(ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True)
    respondent = relationship(
        "User",
        primaryjoin="User.id == Answer_option.respondent_id"
    )
    #Question option FK
    option_id = Column(ForeignKey("question_option.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)
    option_question_id = Column(ForeignKey("question_option.question_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)
    option_question_survey_id = Column(ForeignKey("question_option.question_survey_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True,nullable=False, unique=True)
    question = relationship(
        "Question_option",
        primaryjoin="and_(Question_option.id == Answer_option.option_id, Question_option.question_id == Answer_option.option_question_id, Question_option.question_survey_id == Answer_option.option_question_survey_id)"
    )
    # respondent = relationship("User", foreign_keys=[respondent_id])
    # option = relationship("Question_option", foreign_keys=[option_id])
    # option_question = relationship("Question_option", foreign_keys=[option_question_id])
    # option_question_survey = relationship("Question_option", foreign_keys=[option_question_survey_id])
    
    weight_elected = Column(Integer, nullable=False)

    __table_args__ = (
            UniqueConstraint("respondent_id", "option_id", "option_question_id", "option_question_survey_id",),
        )
    __mapper_args__ = {
        'polymorphic_identity': 'answer_option',
        'inherit_condition': (option_id == Question_option.id, option_question_id == Question_option.question_id, option_question_survey_id == Question_option.question_survey_id)
    }
    #respondents = relationship("User", back_populates="answer_options")
    #question_options_answer = relationship("Question_option", back_populates="answers")