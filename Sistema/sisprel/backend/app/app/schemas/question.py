from pydantic import  BaseModel
from typing import List, Dict, Any, Optional, Set

from .question_option import QuestionOption
from .question_option_open import QuestionOptionOpen

class QuestionBase(BaseModel):
    question: Optional[str] = None
    accept_open_answer: Optional[bool] = False
    is_mandatory: Optional[bool] = True
    

class QuestionCreate(QuestionBase):
    question: str

class QuestionUpdate(QuestionBase):
    pass

class QuestionInDBBase(QuestionBase):
    id: Optional[int]
    question: Optional[str]
    survey_id: Optional[int]
    question_options: Optional[List[QuestionOption]] = []
    question_option_open: QuestionOptionOpen = None

    class Config:
        orm_mode = True

class Question(QuestionInDBBase):
    pass

class QuestionInDB(QuestionInDBBase):
    pass