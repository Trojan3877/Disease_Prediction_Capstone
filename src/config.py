# src/config.py
"""
Configuration file for managing constants, file paths, and random seeds.
"""

import os

# Set base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths
DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'dataset.csv')
MODEL_DIR = os.path.join(BASE_DIR, '..', 'models')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'outputs')

# Create directories if they don't exist
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Set random seed for reproducibility
RANDOM_SEED = 42
