"""
data_loader.py

Module for loading the PIMA Diabetes dataset into a pandas DataFrame.
"""

import pandas as pd

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
