# src/preprocessing.py
"""
Preprocessing module to clean, transform, and prepare data for model training.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path):
    """
    Load the dataset from a CSV file.
    """
    return pd.read_csv(path)

def preprocess_data(df, target_column):
    """
    Preprocess the dataset: separate features/labels, scale features, split data.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Standardize the feature set
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)
