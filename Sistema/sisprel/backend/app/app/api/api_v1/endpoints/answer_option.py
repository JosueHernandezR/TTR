from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.operators import desc_op
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/create-answer-option", response_model=schemas.AnswerOption)
def createAnswerOption(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.AnswerOptionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    option_id: int,
    option_question_id: int,
    option_question_survey_id: int,
) -> Any:
    answer_option = crud.answer_option.createAnswerOption(
        db=db,
        obj_in=obj_in,
        respondent_id=current_user.id,
        option_id=option_id,
        option_question_id=option_question_id,
        option_question_survey_id=option_question_survey_id,
    )
    return answer_option

@router.post("/create-result-aceptacion", response_model=schemas.SurveyAceptacion)
def createAceptacion(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.SurveyAceptacionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    survey_id: int,
) -> Any:
    survey = crud.survey.get(db=db, id=survey_id)
    survey_weight_max = survey.weight_total
    sum_result = crud.answer_option.weight_total_by_survey_and_respondent(
        db=db, option_question_survey_id=survey_id,
        respondent_id=current_user.id,
    )

    aceptacion = crud.survey_aceptacion.createSurveyAceptacion(
        db=db,
        obj_in=obj_in,
        survey_id=survey_id,
        respondent_id=current_user.id,
        sum_weight_answers=sum_result,
        survey_weigth_max=survey_weight_max
    )
    return aceptacion

@router.get("/get-answers-by-survey", response_model=List[schemas.AnswerOption])
def read_answers_by_survey(
    option_question_survey_id:int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    answers_by_survey = crud.answer_option.get_multi_by_survey(
        db = db,
        option_question_survey_id=option_question_survey_id,
        skip=skip,
        limit=limit
    )

    if not answers_by_survey:
        raise HTTPException(status_code=404, detail="Respuestas no encontradas")
    
    return answers_by_survey

@router.get("/get-answers-by-survey-and-respondent", response_model=List[schemas.AnswerOption])
def read_answers_by_survey_and_respondent(
    option_question_survey_id:int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    answers_by_survey_and_respondent = crud.answer_option.get_multi_by_survey_and_respondent(
        db= db,
        option_question_survey_id=option_question_survey_id,
        respondent_id=current_user.id,
        skip=skip,
        limit=limit,
    )

    if not answers_by_survey_and_respondent:
        raise HTTPException(status_code=404, detail="Respuestas no encontradas")

    return answers_by_survey_and_respondent

#Test
@router.get("/consult-a-sum")
def get_a_sum(
    option_question_survey_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
):
    sum_result = crud.answer_option.weight_total_by_survey_and_respondent(
        db=db, option_question_survey_id=option_question_survey_id,
        respondent_id=current_user.id,
    )
    return sum_result