import yaml
import joblib
from pathlib import Path
from src.utils.logger import get_logger
from src.utils.exceptions import ModelLoadError

logger = get_logger(__name__)

def load_config():
    """Loads YAML config file."""
    try:
        with open("config.yaml", "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"❌ Failed to load config.yaml: {e}")
        raise

def load_model(model_path: str):
    """Loads a trained ML model from file."""
    path = Path(model_path)
    try:
        logger.info(f"Loading model from {path}...")
        model = joblib.load(path)
        logger.info("Model loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"❌ Failed to load model: {e}")
        raise ModelLoadError(f"Could not load model at {path}")
