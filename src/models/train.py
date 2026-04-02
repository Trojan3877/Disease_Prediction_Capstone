"""Proxy module — re-exports train_models from the root-level train module."""
from train import train_models

__all__ = ["train_models"]
