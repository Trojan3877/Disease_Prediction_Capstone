import mlflow
import mlflow.sklearn
import xgboost as xgb
import lightgbm as lgb
import yaml
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

from src.data.load_data import load_data
from src.data.preprocess import preprocess_data
from src.data.split import split_data
from src.features.feature_engineering import feature_engineering
from src.models.model_utils import save_model, load_config
from src.utils.logger import get_logger
from src.utils.exceptions import ModelTrainingError

logger = get_logger(__name__)

def train_models():
    try:
        config = load_config()

        logger.info("===== Starting Training Pipeline =====")

        # Load data
        df = load_data()

        # Feature engineering
        X, y, _ = feature_engineering(df)

        # Train-test split
        X_train, X_test, y_train, y_test = split_data(X, y)

        algorithms = config["model_training"]["algorithms"]

        model_candidates = {}
        best_auc = -1
        best_model = None
        best_name = ""

        mlflow.set_tracking_uri(config["mlflow"]["tracking_uri"])
        mlflow.set_experiment(config["mlflow"]["experiment_name"])

        for algo in algorithms:
            with mlflow.start_run():
                logger.info(f"Training: {algo}")

                if algo == "logistic_regression":
                    params = config["model_training"]["logistic_regression"]
                    model = LogisticRegression(C=params["C"], max_iter=params["max_iter"])

                elif algo == "random_forest":
                    params = config["model_training"]["random_forest"]
                    model = RandomForestClassifier(
                        n_estimators=params["n_estimators"],
                        max_depth=params["max_depth"],
                        random_state=params["random_state"],
                    )

                elif algo == "xgboost":
                    params = config["model_training"]["xgboost"]
                    model = xgb.XGBClassifier(
                        n_estimators=params["n_estimators"],
                        learning_rate=params["learning_rate"],
                        max_depth=params["max_depth"],
                        subsample=params["subsample"],
                        colsample_bytree=params["colsample_bytree"],
                        eval_metric="logloss",
                    )

                elif algo == "lightgbm":
                    params = config["model_training"]["lightgbm"]
                    model = lgb.LGBMClassifier(
                        num_leaves=params["num_leaves"],
                        learning_rate=params["learning_rate"],
                        n_estimators=params["n_estimators"],
                    )

                # Fit model
                model.fit(X_train, y_train)

                # Evaluate AUC
                y_pred_prob = model.predict_proba(X_test)[:, 1]
                auc = roc_auc_score(y_test, y_pred_prob)

                logger.info(f"{algo} AUC = {auc:.4f}")
                mlflow.log_metric("AUC", auc)

                if auc > best_auc:
                    best_auc = auc
                    best_model = model
                    best_name = algo

        logger.info(f"Best model selected: {best_name} (AUC={best_auc:.4f})")

        # Save best model
        model_path = config["paths"]["model_file"]
        save_model(best_model, model_path)

        # Save XGB + LGBM formats separately
        if best_name == "xgboost":
            best_model.save_model(config["paths"]["xgb_model_file"])
        if best_name == "lightgbm":
            best_model.booster_.save_model(config["paths"]["lgbm_model_file"])

        logger.info("===== Training Complete =====")
        return best_model, best_auc

    except Exception as e:
        logger.error(f"Training pipeline failed: {e}")
        raise ModelTrainingError(str(e))
