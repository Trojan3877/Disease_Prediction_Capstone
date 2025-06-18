# tests/test_api.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Disease Prediction API!"}

def test_predict_endpoint():
    sample_input = {
        "age": 45,
        "gender": 1,
        "bmi": 29.5,
        "blood_pressure": 85,
        "glucose": 140,
        "insulin": 80,
        "skin_thickness": 32
    }
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], int)
