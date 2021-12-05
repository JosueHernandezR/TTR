from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.ResultPrediction)
def createSurveyResultPrediction(
    *,
    db: Session = Depends(deps.get_db),
    prediction_in: schemas.ResultPredictionCreate,
    survey_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
    ) -> Any:
    survey_result_prediction = crud.survey_result.createSurveyResults(
        db = db,
        obj_in = prediction_in,
        survey_id = survey_id,
    )
    return survey_result_prediction

# Leer las predicciones de una encuesta
@router.get("/all", response_model=List[schemas.ResultPrediction])
def read_all_results_for_a_survey(
    survey_id: int,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int= 100,
    current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    """
    Obtener todos los resultados de una encuesta
    """
    survey_results_prediction = crud.survey_result.get_multi_by_survey(
        db=db,
        survey_id=survey_id,
        skip=skip,
        limit=limit
    )
    return survey_results_prediction

# Leer una predicción
@router.get("/{id}", response_model=schemas.ResultPrediction)
def read_a_result_survey(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get result survey by ID
    """
    survey_result_prediction = crud.survey_result.get(db=db, id=id)
    if not survey_result_prediction:
        raise HTTPException(
            status_code=404,
            detail="Predicción no encontrada"
        )
    # Desarrollar la funcion de obtener la encuesta con el id
    return survey_result_prediction

# Eliminar un resultado de una encuesta
@router.delete("/{id}", response_model=schemas.ResultPrediction)
def delete_survey_result(
    *,
    db:Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
    survey_result_prediction = crud.survey_result.get(db=db, id=id)
    if not survey_result_prediction:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")
    
    return survey_result_prediction

