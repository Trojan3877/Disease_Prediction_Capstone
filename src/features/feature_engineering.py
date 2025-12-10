import pandas as pd
import numpy as np
import joblib
import yaml
from pathlib import Path
from sklearn.preprocessing import PolynomialFeatures
from src.utils.logger import get_logger
from src.utils.exceptions import FeatureEngineeringError

logger = get_logger(__name__)

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def add_medical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds clinically meaningful engineered features.
    These improve predictive accuracy for diabetes models.
    """
    logger.info("Adding medically meaningful engineered features...")

    df = df.copy()

    # BMI Risk Bucket (0–3)
    df["BMI_Risk"] = pd.cut(
        df["BMI"],
        bins=[0, 18.5, 25, 30, 100],
        labels=[0, 1, 2, 3],
        include_lowest=True
    ).astype(int)

    # Glucose × BMI interaction (highly correlated with diabetes)
    df["Glucose_BMI_Interaction"] = df["Glucose"] * df["BMI"]

    # Insulin resistance proxy (HOMA-IR approximation)
    df["IR_Proxy"] = (df["Glucose"] * df["Insulin"]) / 405

    # Age Groups
    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[0, 30, 40, 50, 60, 120],
        labels=[0, 1, 2, 3, 4],
        include_lowest=True
    ).astype(int)

    return df


def generate_polynomial_features(X: pd.DataFrame) -> pd.DataFrame:
    """
    Optionally generates polynomial features using scikit-learn.
    This is disabled by default due to possible model complexity.
    """
    config = load_config()
    poly_enabled = config["preprocessing"].get("feature_engineering", False)

    if not poly_enabled:
        return X

    logger.info("Generating polynomial features (degree=2)...")

    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X)

    return pd.DataFrame(X_poly)


def feature_engineering(df: pd.DataFrame):
    """
    Full feature engineering pipeline:
      - Medical domain features
      - Optional polynomial expansion
      - Scaling (load or create scaler)
    """
    try:
        logger.info("Starting feature engineering...")

        config = load_config()
        scaler_path = Path(config["paths"]["scaler_file"])

        # 1. Add medically significant features
        df = add_medical_features(df)

        # 2. Separate features & target
        X = df.drop("Outcome", axis=1)
        y = df["Outcome"]

        # 3. Polynomial features (optional)
        X = generate_polynomial_features(X)

        # 4. Scaling logic
        scaler = None
        if config["preprocessing"]["scaling"]:
            if scaler_path.exists():
                logger.info("Loading existing scaler...")
                scaler = joblib.load(scaler_path)
                X = scaler.transform(X)
            else:
                from sklearn.preprocessing import StandardScaler

                logger.info("Creating new scaler...")
                scaler = StandardScaler()
                X = scaler.fit_transform(X)
                joblib.dump(scaler, scaler_path)
                logger.info(f"Scaler saved at {scaler_path}")

        logger.info("Feature engineering completed successfully.")
        return X, y, scaler

    except Exception as e:
        logger.error(f"Feature engineering failed: {e}")
        raise FeatureEngineeringError("Failed during feature engineering.")
