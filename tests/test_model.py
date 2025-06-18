# tests/test_model.py

import pytest
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

# Load test data and model
model = joblib.load('models/disease_model.pkl')
test_data = pd.read_csv('data/processed/test_set.csv')
X_test = test_data.drop('disease', axis=1)
y_test = test_data['disease']

def test_model_accuracy():
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    assert accuracy >= 0.85, f"Model accuracy too low: {accuracy:.2f}"
    print(f"✅ Accuracy test passed with {accuracy:.2f}")

def test_model_shape():
    predictions = model.predict(X_test)
    assert len(predictions) == len(y_test), "Mismatch in prediction count"

def test_model_edge_case():
    edge_case = X_test.iloc[0:1].copy()
    result = model.predict(edge_case)
    assert result.shape == (1,), "Edge case prediction failed"
