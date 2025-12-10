<div align="center">

# 🩺🔬 **Diabetes Prediction Platform**  
### **ML + LLM + RAG + MCP + FastAPI + Docker + CI/CD**

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge)
![XGBoost](https://img.shields.io/badge/XGBoost-Boosting-red?style=for-the-badge)
![LightGBM](https://img.shields.io/badge/LightGBM-Models-green?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-VectorStore-blueviolet?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-black?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-API-teal?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge)
![MCP](https://img.shields.io/badge/MCP-Model_Context_Protocol-purple?style=for-the-badge)
![MLflow](https://img.shields.io/badge/MLflow-Experiment_Tracking-lightgrey?style=for-the-badge)
![CI/CD](https://img.shields.io/badge/GitHub-Actions-black?style=for-the-badge)
<p align="center">
  <img src="https://raw.githubusercontent.com/Trojan3877/asset-storage/main/banners/diabetes_prediction_dark.png" 
       alt="Diabetes Prediction System - Dark Banner" width="100%">

---

### 🔥 **A Full-Stack AI System for Clinical Machine Learning**  
Built by **Corey Leath**  
</div>

---

# 🧠 **Overview**

The **Diabetes Prediction Platform** is a full production-grade AI system integrating:

- **Traditional ML models (LogReg, RF, XGBoost, LightGBM)**  
- **LLM-powered medical explanations (GPT-4o-mini)**  
- **RAG (Retrieval-Augmented Generation) with FAISS vector search**  
- **MCP server** for tool calling by ChatGPT, VS Code, Cursor  
- **FastAPI deployment**  
- **Docker containerization**  
- **CI/CD pipeline via GitHub Actions**  
- **MLflow experiment tracking**  

This system delivers:

✔ Predictive diabetes risk  
✔ LLM-generated natural language medical explanations  
✔ Ability to retrain the model through API or MCP tools  
✔ Transparent metrics and model selection  
✔ Modular architecture used in FAANG ML Engineering  

---

# 🏗 **System Architecture**

             ┌──────────────────────────────┐
             │        RAG Subsystem         │
             │  FAISS + Embeddings + LLM    │
             └──────────────┬───────────────┘
                            │
                            ▼
┌──────────────┐ ┌──────────────────────┐ ┌───────────────────────┐
│ ML Pipeline │◀────▶│ FastAPI Application │◀──────▶│ MCP Tool Server │
│ Training & │ │ /predict /rag /train│ │ predict / rag / train │
│ Inference │ └──────────────────────┘ └───────────────────────┘
└──────────────┘ │
▼
┌─────────────────────┐
│ Docker Container │
└─────────────────────┘

> _Architecture diagram placeholder — you may replace with a PNG later._
## 🏗️ System Architecture

https://raw.githubusercontent.com/Trojan3877/asset-storage/main/diagrams/diabetes_architecture_dark.png

## 🔬 Machine Learning Pipeline

<p align="center">
  <img src="https://raw.githubusercontent.com/Trojan3877/asset-storage/main/diagrams/diabetes_ml_pipeline_dark.png"
       alt="Machine Learning Pipeline Diagram - Diabetes Prediction"
       width="95%">
</p>

## 🧠 RAG + LLM Intelligence Layer

<p align="center">
  <img src="https://raw.githubusercontent.com/Trojan3877/asset-storage/main/diagrams/diabetes_rag_flow_dark.png"
       alt="RAG + LLM Flow Diagram - Diabetes Prediction System"
       width="95%">
</p>

---

# 📁 **Project Structure**

Diabetes_Prediction_Capstone/
│
├── README.md
├── metrics.md
├── config.yaml
├── requirements.txt
├── LICENSE
│
├── src/
│ ├── data/ (loading, preprocessing, split)
│ ├── features/ (engineering & scaling)
│ ├── models/ (train, predict, evaluate)
│ └── utils/ (logging, config, exceptions)
│
├── rag/
│ ├── ingest.py
│ ├── embed.py
│ └── query.py
│
├── mcp/
│ ├── server.py
│ ├── manifest.json
│ └── openapi.yaml
│
├── api/
│ ├── main.py
│ ├── endpoints/
│ ├── Dockerfile
│ └── docker-compose.yaml
│
├── tests/
└── .github/workflows/ci_cd.yml

---

# 🚀 **Quick Start (pip)**

```bash
pip install -r requirements.txt
python -m api.main
http://localhost:8000
cd api
docker-compose up --build
