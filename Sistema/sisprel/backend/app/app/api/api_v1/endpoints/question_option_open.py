from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.QuestionOptionOpen)
def create_question_option_open(
    *,
    db: Session = Depends(deps.get_db),
    question_option_open_in: schemas.QuestionOptionOpenCreate,
    question_id: int,
    question_survey_id: int,
) -> Any:
    question_option_open = crud.question_option_open.create_question_option_open(db=db, question_option_open=question_option_open_in, question_id=question_id, question_survey_id=question_survey_id)
    return question_option_open

@router.get("/{id}", response_model=schemas.QuestionOptionOpen)
def read_question_option_open(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
    ) -> Any:
    """
    Get question option by ID.
    """
    question_option = crud.question_option_open.get(db=db, id=id)
    if not question_option:
        raise HTTPException(status_code=404, detail="Question Option not found")
    # Desarrollar la funcion de obtener encuesta con el id
    return question_option

@router.put("/{id}", response_model=schemas.QuestionOptionOpen)
def update_question_option_open(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        question_option_in: schemas.QuestionOptionOpenUpdate,
    ) -> Any:
    """
    Update a question option Open.
    """
    question_option = crud.question_option_open.get(db=db, id=id)
    if not question_option:
        raise HTTPException(status_code=404, detail="Question option not found")
    # Desarrollar la funcion de obtener encuesta con el id
    question_option = crud.question_option_open.update(db=db, db_obj=question_option, obj_in=question_option_in)
    return question_option

@router.delete("/{id}", response_model=schemas.QuestionOptionOpen)
def update_question(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
    ) -> Any:
    """
    Delete a question option.
    """
    question_option = crud.question_option_open.get(db=db, id=id)
    if not question_option:
        raise HTTPException(status_code=404, detail="Question not found")
    # Desarrollar la funcion de obtener encuesta con el id
    question_option_open = crud.question_option_open.remove(db=db, id=id)
    return question_option_open
