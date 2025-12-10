from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200

def test_predict_api():
    body = {"features": [5, 120, 70, 20, 80, 32.0, 0.4, 33]}
    response = client.post("/predict/", json=body)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_rag_api():
    body = {"question": "What factors increase diabetes risk?"}
    response = client.post("/rag/", json=body)
    assert response.status_code == 200
    assert "result" in response.json()
