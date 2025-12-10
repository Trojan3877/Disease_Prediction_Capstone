from fastapi import APIRouter
from pydantic import BaseModel
from src.models.predict import predict

router = APIRouter()

class PredictRequest(BaseModel):
    features: list

@router.post("/")
def predict_diabetes(req: PredictRequest):
    """Returns diabetes prediction and probability."""
    result = predict(req.features)
    return {
        "prediction": result["prediction"],
        "probability": result["probability"]
    }
