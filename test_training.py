import pytest
mlflow = pytest.importorskip("mlflow", reason="mlflow not installed; skipping training tests")

from unittest.mock import patch, MagicMock
from train import train_models

@patch("train.load_data")
@patch("train.feature_engineering")
@patch("train.split_data")
@patch("train.save_model")
@patch("train.load_config")
@patch("train.mlflow")
def test_training_pipeline(mock_mlflow, mock_load_config, mock_save_model,
                           mock_split, mock_feat_eng, mock_load_data):
    import numpy as np
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=100, n_features=8, random_state=42)
    X_train, X_test = X[:80], X[80:]
    y_train, y_test = y[:80], y[80:]

    mock_load_config.return_value = {
        "model_training": {
            "algorithms": ["logistic_regression"],
            "logistic_regression": {"C": 1.0, "max_iter": 200},
        },
        "mlflow": {"tracking_uri": "mlruns/", "experiment_name": "test"},
        "paths": {
            "model_file": "/tmp/test_model.pkl",
            "xgb_model_file": "/tmp/xgb.json",
            "lgbm_model_file": "/tmp/lgbm.txt",
        },
    }
    mock_load_data.return_value = None
    mock_feat_eng.return_value = (X, y, None)
    mock_split.return_value = (X_train, X_test, y_train, y_test)
    mock_mlflow.set_tracking_uri = MagicMock()
    mock_mlflow.set_experiment = MagicMock()
    mock_mlflow.start_run = MagicMock()
    mock_mlflow.start_run.return_value.__enter__ = MagicMock(return_value=None)
    mock_mlflow.start_run.return_value.__exit__ = MagicMock(return_value=False)
    mock_mlflow.log_metric = MagicMock()

    model, auc = train_models()

    assert model is not None
    assert 0 <= auc <= 1
