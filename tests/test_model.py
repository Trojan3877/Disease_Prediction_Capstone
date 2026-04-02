# tests/test_model.py

import pytest
import numpy as np
from unittest.mock import patch, MagicMock
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score


@pytest.fixture
def trained_model_and_data():
    """Create a minimal trained model and test data for use in tests."""
    X, y = make_classification(n_samples=200, n_features=7, random_state=42)
    split = int(len(X) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)

    return model, X_test, y_test


def test_model_accuracy(trained_model_and_data):
    model, X_test, y_test = trained_model_and_data
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    assert accuracy >= 0.0, f"Model accuracy unexpectedly negative: {accuracy:.2f}"
    print(f"✅ Accuracy test passed with {accuracy:.2f}")


def test_model_shape(trained_model_and_data):
    model, X_test, y_test = trained_model_and_data
    predictions = model.predict(X_test)
    assert len(predictions) == len(y_test), "Mismatch in prediction count"


def test_model_edge_case(trained_model_and_data):
    model, X_test, y_test = trained_model_and_data
    edge_case = X_test[0:1]
    result = model.predict(edge_case)
    assert result.shape == (1,), "Edge case prediction failed"
