# tests/test_api.py

import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Diabetes Prediction API is running"}

@patch("api.endpoints.predict_endpoint.predict")
def test_predict_endpoint(mock_predict):
    mock_predict.return_value = {"prediction": 1, "probability": 0.75}
    sample_input = {"features": [5, 120, 70, 20, 80, 32.0, 0.4, 33]}
    response = client.post("/predict/", json=sample_input)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], int)
