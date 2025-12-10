import json
from mcp.server.fastapi import FastAPI
from fastapi import Body
from src.models.predict import predict
from src.models.train import train_models
from rag.query import rag_query
from src.utils.logger import get_logger
from src.utils.exceptions import MCPError

logger = get_logger(__name__)

app = FastAPI(
    title="Diabetes Prediction MCP Server",
    description="MCP-enabled ML + RAG + LLM system",
    version="1.0.0"
)

@app.post("/predict")
def predict_tool(data: dict = Body(...)):
    """
    MCP Tool: Predict diabetes risk.
    """
    try:
        input_data = data["features"]
        logger.info(f"MCP Predict Called: {input_data}")
        result = predict(input_data)
        return {"result": result}
    except Exception as e:
        raise MCPError(f"MCP Predict failed: {str(e)}")


@app.post("/retrain")
def retrain_tool():
    """
    MCP Tool: Retrains the ML pipeline.
    """
    try:
        logger.info("MCP Retrain Called")
        model, auc = train_models()
        return {"status": "success", "best_auc": auc}
    except Exception as e:
        raise MCPError(f"MCP Retrain failed: {str(e)}")


@app.post("/rag_query")
def rag_query_tool(data: dict = Body(...)):
    """
    MCP Tool: LLM-backed medical explanation.
    """
    try:
        question = data["question"]
        logger.info(f"MCP RAG Query: {question}")
        response = rag_query(question)
        return {"result": response}
    except Exception as e:
        raise MCPError(f"MCP RAG Query failed: {str(e)}")


# MCP server launcher
def start_server():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9001)
