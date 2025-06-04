"""
utils.py

Utility functions for plotting and common tasks.
"""

def ensure_dir(directory):
    """
    Create directory if it doesn't exist.
    
    Args:
        directory (str): Path of the directory to create.
    """
    import os
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
