# tests/test_predict.py
"""
Unit tests for the Disease Prediction API endpoint using FastAPI and Pytest.
"""

from fastapi.testclient import TestClient
from predict import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Disease Prediction API"}

def test_predict_positive():
    data = {
        "age": 55,
        "bmi": 32.5,
        "blood_pressure": 145,
        "cholesterol": 210,
        "glucose": 130
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_negative():
    data = {
        "age": 25,
        "bmi": 21.4,
        "blood_pressure": 110,
        "cholesterol": 170,
        "glucose": 85
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()
