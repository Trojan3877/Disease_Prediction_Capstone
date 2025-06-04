"""
preprocessing.py

Module for preprocessing and feature engineering of the PIMA Diabetes dataset.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Preprocess the input DataFrame:
    - Handle missing values (replace zeros with median for certain columns).
    - Scale numerical features using StandardScaler.
    - Return processed feature array, target array, and scaler object.

    Args:
        df (pandas.DataFrame): Raw input DataFrame.

    Returns:
        X_scaled (numpy.ndarray): Scaled feature array.
        y (pandas.Series): Target array.
        scaler (StandardScaler): Fitted scaler object.
    """
    # Replace zeros (invalid values) with median for specific columns
    for col in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']:
        df[col] = df[col].replace(0, df[col].median())
    
    # Separate features and target
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, scaler
