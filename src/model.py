"""
model.py

Module for defining and training machine learning models:
- Logistic Regression
- XGBoost Classifier
"""

from sklearn.linear_model import LogisticRegression
import xgboost as xgb

def get_logistic_regression_model():
    """
    Initialize a Logistic Regression model.
    
    Returns:
        LogisticRegression: Untrained logistic regression model.
    """
    lr = LogisticRegression(solver='liblinear', random_state=42)
    return lr

def get_xgboost_model():
    """
    Initialize an XGBoost Classifier model.
    
    Returns:
        XGBClassifier: Untrained XGBoost classifier.
    """
    xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    return xgb_model
