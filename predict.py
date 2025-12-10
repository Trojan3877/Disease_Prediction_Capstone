import numpy as np
import joblib
from src.utils.logger import get_logger
from src.utils.helpers import load_config
from src.utils.exceptions import PredictionError

logger = get_logger(__name__)

def predict(input_data):
    try:
        config = load_config()

        model = joblib.load(config["paths"]["model_file"])
        scaler_path = config["paths"]["scaler_file"]

        if Path(scaler_path).exists():
            scaler = joblib.load(scaler_path)
            input_data = scaler.transform([input_data])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        logger.info(f"Prediction: {prediction}, Prob={probability:.4f}")

        return {
            "prediction": int(prediction),
            "probability": float(probability)
        }

    except Exception as e:
        raise PredictionError(f"Prediction failed: {e}")
