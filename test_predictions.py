import numpy as np
from unittest.mock import patch, MagicMock
from predict import predict

@patch("predict.joblib.load")
@patch("predict.load_config")
def test_prediction_output(mock_load_config, mock_joblib_load, tmp_path):
    mock_load_config.return_value = {
        "paths": {
            "model_file": str(tmp_path / "model.pkl"),
            "scaler_file": str(tmp_path / "scaler.pkl"),
        }
    }

    mock_model = MagicMock()
    mock_model.predict.return_value = np.array([1])
    mock_model.predict_proba.return_value = np.array([[0.2, 0.8]])
    mock_joblib_load.return_value = mock_model

    sample = [5, 120, 70, 20, 80, 32.0, 0.4, 33]
    result = predict(sample)

    assert "prediction" in result
    assert "probability" in result
    assert result["prediction"] in [0, 1]
    assert 0 <= result["probability"] <= 1
