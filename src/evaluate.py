# src/evaluate.py
"""
Evaluate a trained Random Forest model using test data.
"""

import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from src.config import MODEL_DIR, DATA_PATH
from src.preprocessing import load_data, preprocess_data

def evaluate_model():
    """
    Load the saved model and evaluate it on test data.
    """
    model_path = f"{MODEL_DIR}/random_forest_model.pkl"
    model = joblib.load(model_path)

    df = load_data(DATA_PATH)
    X_train, X_test, y_train, y_test = preprocess_data(df, target_column='target')

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)

    print(f"Accuracy: {acc}")
    print("Confusion Matrix:\n", cm)
    print("Classification Report:\n", cr)

if __name__ == "__main__":
    evaluate_model()

    
    
