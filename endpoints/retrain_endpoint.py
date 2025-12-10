from fastapi import APIRouter
from src.models.train import train_models

router = APIRouter()

@router.post("/")
def retrain_model():
    """Runs full training pipeline and updates models."""
    model, auc = train_models()
    return {
        "status": "success",
        "best_auc": auc
    }
