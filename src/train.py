"""
train.py

Script for training models on the PIMA Diabetes dataset. Implements:
- Data loading
- Preprocessing
- Train/Test split
- 5-fold cross-validation
- Model fitting
- Saving trained model to disk
"""

import argparse
import os
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import get_logistic_regression_model, get_xgboost_model

def train_and_evaluate(data_path, output_model_path):
    """
    Train and evaluate Logistic Regression and XGBoost models.

    Args:
        data_path (str): Path to the raw CSV data.
        output_model_path (str): Path to save the best trained model.
    """
    # Load data
    df = load_data(data_path)
    
    # Preprocess data
    X, y, scaler = preprocess_data(df)
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize models
    lr_model = get_logistic_regression_model()
    xgb_model = get_xgboost_model()
    
    # 5-fold cross-validation on training set
    for model, name in [(lr_model, 'Logistic Regression'), (xgb_model, 'XGBoost')]:
        scores = cross_val_score(model, X_train, y_train, cv=5, scoring='roc_auc')
        print(f"{name} CV ROC AUC scores: {scores}")
        print(f"{name} CV ROC AUC mean: {scores.mean():.4f}")
    
    # Train XGBoost on full training set (example)
    xgb_model.fit(X_train, y_train)
    
    # Save trained model
    os.makedirs(os.path.dirname(output_model_path), exist_ok=True)
    joblib.dump((xgb_model, scaler), output_model_path)
    print(f"Model saved to {output_model_path}")

def main():
    parser = argparse.ArgumentParser(description="Train models for PIMA Diabetes Prediction")
    parser.add_argument('--data_path', type=str, required=True, help='Path to input CSV file')
    parser.add_argument('--output_model', type=str, required=True, help='Path to save trained model')
    args = parser.parse_args()
    
    train_and_evaluate(args.data_path, args.output_model)

if __name__ == "__main__":
    main()
