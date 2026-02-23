from fastapi import APIRouter, Depends, HTTPException
from app.schemas.predictions_schema import Prediction, PredictionCreate
from app.services.sentiment_services import predict_sentiment
from app.utils.logger import get_logger
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.models.predictions_model import Prediction as PredictionsModel  # Import the model if needed for database operations

logging = get_logger(__name__)
router = APIRouter(prefix="/sentiment", tags=["Sentiment Analysis"])


@router.post("/predict", response_model=Prediction)
def predict_route(
    request: PredictionCreate,  db: Session = Depends(get_db)  # Dependency to get the database session, if needed
):
    """
    Predict the sentiment of the input text.
    :param prediction: The input text to analyze.
    :return: A dictionary with the sentiment label and score.
    """


    logging.info(f"Received prediction request: {request.text}")
    result = predict_sentiment(request.text)
    db_prediction_item = PredictionsModel(text_content=request.text, pred_value=result['label'])
    
    try:
        db.add(db_prediction_item)
        db.commit()  # Commit the transaction to save the prediction in the database
        db.refresh(db_prediction_item)
        logging.info(f"Prediction result: {result}")
        return Prediction(text=request.text, sentiment=result['label'])
    except Exception as e:
        db.rollback()
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred")


@router.get("/")
def get_all_predictions(db: Session = Depends(get_db)):
    logging.info("Fetching all predictions from the database.")
    try:
        predictions = db.query(PredictionsModel).all()
        return [
            {
                "id": pred.id,
                "text_content": pred.text_content,
                "prediction_label": pred.pred_value  # ← FIXED: use pred_value
            }
            for pred in predictions
        ]
    except Exception as e:
        logging.error(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=str(e))