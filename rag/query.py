"""Proxy module — re-exports rag_query from the root-level query module."""
from query import rag_query

__all__ = ["rag_query"]
