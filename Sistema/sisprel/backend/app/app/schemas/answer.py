from datetime import datetime
from typing import Optional, List

from pydantic import UUID4, BaseModel, EmailStr

class AnswerBase(BaseModel):
    weight: int
    open_answer: Optional[str]
    option_id: Optional[int] = None


class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(AnswerBase):
    pass

class AnswerInDBBase(AnswerBase):
    id: int
    question_id: int
    surveyed_id: int
    answered_at: datetime

    class Config:
        orm_mode = True

class Answer(AnswerInDBBase):
    pass

class AnswerInDB(AnswerInDBBase):
    pass