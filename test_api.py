import importlib.util
import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200

@patch("api.endpoints.predict_endpoint.predict")
def test_predict_api(mock_predict):
    mock_predict.return_value = {"prediction": 1, "probability": 0.75}
    body = {"features": [5, 120, 70, 20, 80, 32.0, 0.4, 33]}
    response = client.post("/predict/", json=body)
    assert response.status_code == 200
    assert "prediction" in response.json()

@pytest.mark.skipif(
    importlib.util.find_spec("openai") is None,
    reason="openai not installed; skipping RAG endpoint test"
)
@patch("api.endpoints.rag_query_endpoint.rag_query")
def test_rag_api(mock_rag):
    mock_rag.return_value = {"answer": "High glucose is a key risk factor.", "sources": []}
    body = {"question": "What factors increase diabetes risk?"}
    response = client.post("/rag/", json=body)
    assert response.status_code == 200
