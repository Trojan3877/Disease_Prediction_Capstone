from fastapi import FastAPI
from api.endpoints.predict_endpoint import router as predict_router
from api.endpoints.rag_query_endpoint import router as rag_router
from api.endpoints.retrain_endpoint import router as retrain_router

app = FastAPI(
    title="Diabetes Prediction API",
    description="ML + RAG + LLM powered medical support system",
    version="1.0.0"
)

# Register API endpoints
app.include_router(predict_router, prefix="/predict", tags=["Prediction"])
app.include_router(rag_router, prefix="/rag", tags=["RAG"])
app.include_router(retrain_router, prefix="/retrain", tags=["Training"])

@app.get("/")
def root():
    return {"message": "Diabetes Prediction API is running"}
