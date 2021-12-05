from typing import TYPE_CHECKING
from sqlalchemy.sql.expression import null

from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from app.db.base_class import Base
from sqlalchemy import Column, Text, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .question import Question  # noqa: F401

class Question_option(Base):
    __mapper_args__ = {'polymorphic_identity': 'question_option'}
    
    id = Column(Integer, primary_key=True, nullable= False, index=True, unique=True, autoincrement=True)
    option_name = Column(String(3), nullable=False)
    option = Column(Text, nullable=False)
    weight = Column(Integer(), nullable=False)

    #question_id = Column(Integer, ForeignKey("question.id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True, index=True)
    question_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    #question_survey_id = Column(Integer, ForeignKey("question.survey_id", onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False, unique=True, index=True)
    question_survey_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    
    question = relationship(
        "Question",
        foreign_keys='Question_option.question_id',
        backref='question_option'
    )
    question_survey = relationship(
        "Question",
        foreign_keys='Question_option.question_survey_id',
        backref='question_option'
    )
    # question = relationship(
    #     "Question", 
    #     foreign_keys='[Question_option.question_id, Question_option.question_survey_id]',
    #     primaryjoin="and_(Question.id == Question_option.question_id, Question.survey_id == Question_option.question_survey_id)",
    #     backref='question_option'
    # )
    #question_survey = relationship("Question", foreign_keys='Question_option.question_survey_id')

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
    #questions = relationship("Question", back_populates="question_options")
    #answers = relationship("Answer_Option", back_populates="question_options_answer")
    #answers = relationship("Answer_Option",)
    
    users = relationship(
        'User',
        secondary="answer_option",
        backref="question_option",
        
    )
