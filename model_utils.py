import joblib
import yaml
from pathlib import Path
from src.utils.logger import get_logger
from src.utils.exceptions import ModelTrainingError

logger = get_logger(__name__)

def load_config():
    """Load YAML config."""
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def save_model(model, path: str):
    """Save trained model."""
    try:
        joblib.dump(model, path)
        logger.info(f"Model saved at {path}")
    except Exception as e:
        raise ModelTrainingError(f"Failed to save model: {e}")
