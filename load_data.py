import pandas as pd
import yaml
from pathlib import Path
from src.utils.logger import get_logger
from src.utils.exceptions import DataLoadError

logger = get_logger(__name__)

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def load_data():
    """Loads raw diabetes dataset and returns a DataFrame."""
    config = load_config()
    data_path = Path(config["paths"]["raw_data"])

    try:
        logger.info(f"Loading dataset from {data_path}...")
        df = pd.read_csv(data_path)
        logger.info(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
        return df

    except Exception as e:
        logger.error(f"Failed to load dataset: {e}")
        raise DataLoadError(f"Unable to read data file at {data_path}")
