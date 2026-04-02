"""Proxy module — re-exports model utilities from the root-level model_utils module."""
from model_utils import save_model, load_config

__all__ = ["save_model", "load_config"]
