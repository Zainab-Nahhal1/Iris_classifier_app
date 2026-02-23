from pydantic import BaseModel

class ModelInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float

class ModelOutput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    pred_value: float
