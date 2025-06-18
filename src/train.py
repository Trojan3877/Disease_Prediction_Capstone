# src/train.py
"""
Model training script using Random Forest Classifier.
"""

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from src.config import DATA_PATH, MODEL_DIR
from src.preprocessing import load_data, preprocess_data

def train_model():
    """
    Load data, preprocess it, train a Random Forest model, and save it.
    """
    df = load_data(DATA_PATH)
    X_train, X_test, y_train, y_test = preprocess_data(df, target_column='target')

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)

    print("Model Accuracy:", acc)
    print("Classification Report:\n", classification_report(y_test, predictions))

    # Save the model
    model_path = f"{MODEL_DIR}/random_forest_model.pkl"
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
