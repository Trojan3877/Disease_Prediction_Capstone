"""
Utility package for the Disease Prediction Capstone project.
"""

import os


def ensure_dir(directory):
    """
    Create directory if it doesn't exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
