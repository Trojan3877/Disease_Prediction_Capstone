import numpy as np
from src.models.predict import predict

def test_prediction_output():
    # Sample fake input (8 medical features)
    sample = [5, 120, 70, 20, 80, 32.0, 0.4, 33]

    result = predict(sample)

    assert "prediction" in result
    assert "probability" in result
    assert result["prediction"] in [0, 1]
    assert 0 <= result["probability"] <= 1
