from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.model_schema import ModelInput, ModelOutput
from app.services.ml_services import predict_and_save
from app.dependencies import get_db  # your db dependency

router = APIRouter(prefix="/ml", tags=["Machine Learning"])

@router.post("/predict", response_model=ModelOutput)
def predict_route(input_data: ModelInput, db: Session = Depends(get_db)):
    return predict_and_save(db, input_data)
