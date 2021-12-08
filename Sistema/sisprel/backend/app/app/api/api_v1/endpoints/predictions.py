from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Prediction)
def createPrediction(
    *,
    db: Session = Depends(deps.get_db),
    prediction_in: schemas.PredictionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    prediction = crud.prediction_manual.createPredictionManual(
        db=db,
        obj_in=prediction_in,
        owner_id=current_user.id,
    )
    return prediction

@router.get("/all", response_model=List[schemas.Prediction])
def read_all_predictions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    predictions = crud.prediction_manual.get_multi(
        db=db,
        skip=skip,
        limit=limit,
    )
    return predictions

@router.get("/", response_model=List[schemas.Prediction])
def read_all_predictions_by_owner(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    predictions = crud.prediction_manual.get_multi_by_owner(
        db = db,
        owner_id=current_user.id,
        skip=skip,
        limit=limit
    )
    return predictions

# Leer una predicción
@router.get("/{id}", response_model=schemas.ResultPrediction)
def read_a_prediction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get result survey by ID
    """
    prediction = crud.prediction_manual.get(db=db, id=id)
    if not prediction:
        raise HTTPException(
            status_code=404,
            detail="Predicción no encontrada"
        )
    # Desarrollar la funcion de obtener la encuesta con el id
    return prediction

@router.delete("/{id}", response_model=schemas.Prediction)
def delete_prediction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    ) -> Any:
        prediction = crud.prediction_manual.get(db=db, id=id)
        if not prediction:
            raise HTTPException(status_code=404, detail="Predicción no encontrada")
        if (prediction.owner_id != current_user.id):
            raise HTTPException(status_code=400, detail="No tienes los permisos")
        
        prediction = crud.prediction_manual.remove(db=db, id= id)
        return prediction
