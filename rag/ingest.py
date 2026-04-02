"""Proxy module — re-exports ingest_documents from the root-level ingest module."""
from ingest import ingest_documents, chunk_text

__all__ = ["ingest_documents", "chunk_text"]
