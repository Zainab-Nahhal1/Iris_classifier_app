from sqlalchemy import Column, Integer, Float, String
from app.database import Base  # or wherever your Base is

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    text_content = Column(String, index=True)
    pred_value = Column(String, index=True)
