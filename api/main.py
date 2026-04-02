from fastapi import FastAPI
from src.utils.logger import get_logger
from api.endpoints.predict_endpoint import router as predict_router

logger = get_logger(__name__)

app = FastAPI(
    title="Diabetes Prediction API",
    description="ML + RAG + LLM powered medical support system",
    version="1.0.0"
)

# Register core prediction endpoint
app.include_router(predict_router, prefix="/predict", tags=["Prediction"])

# Retrain endpoint is optional (requires mlflow and full training pipeline)
try:
    from api.endpoints.retrain_endpoint import router as retrain_router
    app.include_router(retrain_router, prefix="/retrain", tags=["Training"])
except ImportError as e:
    logger.warning(f"Retrain endpoint unavailable (missing dependency): {e}")

# RAG endpoint is optional (requires OpenAI + FAISS)
try:
    from api.endpoints.rag_query_endpoint import router as rag_router
    app.include_router(rag_router, prefix="/rag", tags=["RAG"])
except ImportError as e:
    logger.warning(f"RAG endpoint unavailable (missing dependency): {e}")

@app.get("/")
def root():
    return {"message": "Diabetes Prediction API is running"}
