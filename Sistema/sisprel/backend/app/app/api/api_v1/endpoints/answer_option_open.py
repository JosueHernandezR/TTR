from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.AnswerOptionOpen)
def  createAnswerOptionOpen(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.AnswerOptionOpenCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    option_id: int,
    option_question_id: int,
    option_question_survey_id: int,
) -> Any:
    answer_option_open = crud.answer_option_open.createAnswerOptionOpen(
        db=db,
        obj_in=obj_in,
        respondent_id=current_user.id,
        option_id=option_id,
        option_question_id=option_question_id,
        option_question_survey_id=option_question_survey_id,
    )
    return answer_option_open

@router.get("/", response_model=List[schemas.AnswerOptionOpen])
def read_answers_by_survey_and_respondent(
    option_question_survey_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    answers_open_by_survey_and_respondent = crud.answer_option_open.get_multi_by_survey_and_respondent(
        db=db,
        option_question_survey_id=option_question_survey_id,
        respondent_id= current_user.id,
        skip=skip,
        limit=limit,
    )
    if not answers_open_by_survey_and_respondent:
        raise HTTPException(status_code=404, detail="Respuestas no encontradas")
    
    return answers_open_by_survey_and_respondent

