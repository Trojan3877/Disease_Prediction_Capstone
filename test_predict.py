# tests/test_predict.py
"""
Unit tests for the Disease Prediction API endpoint using FastAPI and Pytest.
"""

from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Diabetes Prediction API is running"}

@patch("api.endpoints.predict_endpoint.predict")
def test_predict_positive(mock_predict):
    mock_predict.return_value = {"prediction": 1, "probability": 0.85}
    body = {"features": [5, 130, 80, 32, 80, 32.5, 0.5, 55]}
    response = client.post("/predict/", json=body)
    assert response.status_code == 200
    assert "prediction" in response.json()

@patch("api.endpoints.predict_endpoint.predict")
def test_predict_negative(mock_predict):
    mock_predict.return_value = {"prediction": 0, "probability": 0.12}
    body = {"features": [1, 85, 66, 29, 0, 26.6, 0.35, 31]}
    response = client.post("/predict/", json=body)
    assert response.status_code == 200
    assert "prediction" in response.json()
