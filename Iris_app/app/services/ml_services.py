import os
import joblib
import numpy as np
from sqlalchemy.orm import Session
from app.models.predictions_model import Prediction
from app.schemas.model_schema import ModelInput, ModelOutput

# Properly get the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "models", "iris_model.pkl")

# Load your trained ML model
model = joblib.load(MODEL_PATH)

def to_native(val):
    """Convert NumPy types to native Python types for PostgreSQL."""
    if isinstance(val, np.generic):
        return val.item()
    return val

def predict_and_save(db: Session, input_data: ModelInput) -> ModelOutput:
    # Prepare input for prediction
    features = [
        [
            to_native(input_data.feature1),
            to_native(input_data.feature2),
            to_native(input_data.feature3),
            to_native(input_data.feature4)
        ]
    ]
    
    # Make prediction
    pred_value = to_native(model.predict(features)[0])

    # Save to database
    db_pred = Prediction(
        feature1=features[0][0],
        feature2=features[0][1],
        feature3=features[0][2],
        feature4=features[0][3],
        pred_value=pred_value
    )
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)

    # Return as schema
    return ModelOutput(
        feature1=db_pred.feature1,
        feature2=db_pred.feature2,
        feature3=db_pred.feature3,
        feature4=db_pred.feature4,
        pred_value=db_pred.pred_value
    )
