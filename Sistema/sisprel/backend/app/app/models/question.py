from typing import TYPE_CHECKING
from uuid import uuid4
from sqlalchemy.sql.expression import true

from sqlalchemy.sql.schema import ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, Text, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .survey import Survey  # noqa: F401

class Question(Base):
    __mapper_args__ = {'polymorphic_identity': 'question'}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question = Column(Text,index=True, nullable=False)
    accept_open_answer = Column(Boolean(), nullable=False)
    is_mandatory = Column(Boolean(), default=True, nullable=False)
    
    survey_id = Column(Integer, ForeignKey("survey.id", onupdate="CASCADE", ondelete="CASCADE"), unique=True, index=True)

