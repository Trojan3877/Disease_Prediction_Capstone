from fastapi import APIRouter
from pydantic import BaseModel
from rag.query import rag_query

router = APIRouter()

class RAGRequest(BaseModel):
    question: str

@router.post("/")
def rag_query_api(req: RAGRequest):
    """Queries clinical docs with LLM explanation."""
    result = rag_query(req.question)
    return result
