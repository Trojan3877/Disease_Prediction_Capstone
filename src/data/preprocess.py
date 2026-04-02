"""Proxy module — re-exports preprocess_data from the root-level preprocess module."""
from preprocess import preprocess_data

__all__ = ["preprocess_data"]
