"""
update_data.py

Fetches the latest PIMA Diabetes data (or any remote source), and writes it to `data/raw/`.
Then calls preprocessing to populate `data/processed/` automatically.
"""

import os
import requests
from src.preprocessing import preprocess_data
from src.data_loader import load_data

# 1. Download new data if available
DATA_URL = "https://url.to/updated/pima_diabetes.csv"
RAW_PATH = "data/raw/diabetes.csv"
PROCESSED_DIR = "data/processed/"

def download_latest_data():
    response = requests.get(DATA_URL)
    response.raise_for_status()
    os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)
    with open(RAW_PATH, "wb") as f:
        f.write(response.content)
    print(f"[update_data] Downloaded new data to {RAW_PATH}")

def run_preprocessing():
    df = load_data(RAW_PATH)
    X_scaled, y, scaler = preprocess_data(df)
    # Optionally save X_scaled / y to disk in PROCESSED_DIR, or just leave them for train.py
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    # Example: save processed NumPy arrays for quick training
    import numpy as np
    np.save(os.path.join(PROCESSED_DIR, "X_scaled.npy"), X_scaled)
    np.save(os.path.join(PROCESSED_DIR, "y.npy"), y.to_numpy())
    print(f"[update_data] Preprocessed data saved to {PROCESSED_DIR}")

if __name__ == "__main__":
    download_latest_data()
    run_preprocessing()
