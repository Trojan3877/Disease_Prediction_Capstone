"""
evaluate.py

Script for evaluating a trained model on the PIMA Diabetes dataset. Implements:
- Loading trained model and scaler
- Making predictions
- Generating metrics: accuracy, precision, recall, F1, ROC AUC
- Creating and saving plots: confusion matrix, ROC curve, feature importance
"""

import argparse
import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix
)

def plot_confusion_matrix(y_true, y_pred, output_path):
    """
    Plot and save confusion matrix.
    
    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels.
        output_path (str): Path to save plot.
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig(output_path)
    plt.close()

def plot_roc_curve(y_true, y_probs, output_path):
    """
    Plot and save ROC curve.
    
    Args:
        y_true (array-like): True labels.
        y_probs (array-like): Predicted probabilities for positive class.
        output_path (str): Path to save plot.
    """
    fpr, tpr, _ = roc_curve(y_true, y_probs)
    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, label="ROC Curve")
    plt.plot([0, 1], [0, 1], '--', color='gray')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend(loc="lower right")
    plt.savefig(output_path)
    plt.close()

def plot_feature_importance(model, feature_names, output_path):
    """
    Plot and save feature importance for XGBoost model.
    
    Args:
        model: Trained XGBoost model.
        feature_names (list): List of feature names.
        output_path (str): Path to save plot.
    """
    importance = model.feature_importances_
    sorted_idx = np.argsort(importance)
    plt.figure(figsize=(8, 6))
    plt.barh(np.array(feature_names)[sorted_idx], importance[sorted_idx])
    plt.xlabel("Feature Importance")
    plt.title("Feature Importance (XGBoost)")
    plt.savefig(output_path)
    plt.close()

def evaluate_model(model_path, data_path):
    """
    Evaluate the trained model on test data and save metrics + plots.
    
    Args:
        model_path (str): Path to the saved trained model (includes scaler).
        data_path (str): Path to the raw CSV data.
    """
    # Load model and scaler
    model, scaler = joblib.load(model_path)
    
    # Load test data for evaluation
    from src.data_loader import load_data
    from src.preprocessing import preprocess_data
    df = load_data(data_path)
    X, y, _ = preprocess_data(df)
    
    # Split data (matching train/test logic)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Predict
    y_pred = model.predict(X_test)
    y_probs = model.predict_proba(X_test)[:, 1]
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_probs)
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")
    
    # Generate and save plots
    os.makedirs('results', exist_ok=True)
    plot_confusion_matrix(y_test, y_pred, 'results/confusion_matrix.png')
    plot_roc_curve(y_test, y_probs, 'results/roc_curve.png')
    feature_names = load_data(data_path).drop('Outcome', axis=1).columns
    plot_feature_importance(model, feature_names, 'results/feature_importance.png')

def main():
    parser = argparse.ArgumentParser(description="Evaluate the trained model on test data")
    parser.add_argument('--model_path', type=str, required=True, help='Path to trained model file')
    parser.add_argument('--data_path', type=str, required=True, help='Path to raw CSV file')
    args = parser.parse_args()
    
    evaluate_model(args.model_path, args.data_path)

if __name__ == "__main__":
    main()

  
    
    
