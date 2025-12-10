import pandas as pd
import numpy as np
import joblib
import yaml
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from src.utils.logger import get_logger
from src.utils.exceptions import PreprocessingError

logger = get_logger(__name__)

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def preprocess_data(df: pd.DataFrame):
    """
    Handles missing values, scaling, and feature engineering.
    Returns processed DataFrame and scaler object.
    """
    config = load_config()
    scaler_path = Path(config["paths"]["scaler_file"])

    try:
        logger.info("Starting preprocessing pipeline...")

        # Replace zeros with NaN for medical fields where zero is invalid
        zero_invalid_cols = ["Glucose", "BloodPressure", "BMI", "SkinThickness"]
        df[zero_invalid_cols] = df[zero_invalid_cols].replace(0, np.nan)

        if config["preprocessing"]["handle_missing"]:
            df.fillna(df.mean(), inplace=True)

        # Separate features & target
        X = df.drop("Outcome", axis=1)
        y = df["Outcome"]

        scaler = None
        if config["preprocessing"]["scaling"]:
            scaler = StandardScaler()
            X = scaler.fit_transform(X)
            joblib.dump(scaler, scaler_path)
            logger.info(f"Scaler saved at {scaler_path}")

        logger.info("Preprocessing completed successfully.")
        return X, y, scaler

    except Exception as e:
        logger.error(f"Error during preprocessing: {e}")
        raise PreprocessingError("Failed to preprocess dataset.")
