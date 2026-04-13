![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![ML Pipeline](https://img.shields.io/badge/ML-End--to--End%20Pipeline-orange)
![Classification](https://img.shields.io/badge/Task-Disease%20Prediction-red)
![Data Science](https://img.shields.io/badge/Data%20Science-Production%20Ready-purple)
![Model Evaluation](https://img.shields.io/badge/Metrics-Precision%20%7C%20Recall%20%7C%20F1-blue)
![Healthcare](https://img.shields.io/badge/Industry-Healthcare%20AI-critical)
![Status](https://img.shields.io/badge/Status-Portfolio%20Ready-brightgreen)
![Maintained](https://img.shields.io/badge/Maintained-Yes-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/Trojan3877/Disease_Prediction_Capstone)
![Repo Size](https://img.shields.io/github/repo-size/Trojan3877/Disease_Prediction_Capstone)
![Stars](https://img.shields.io/github/stars/Trojan3877/Disease_Prediction_Capstone?style=social)



This repository contains a **production-ready Machine Learning system** for predicting diabetes using structured clinical features.

Engineered using **FAANG-level best practices**, the system includes:

- End-to-end ML pipeline  
- Vector-store powered RAG explainability  
- LLM reasoning (GPT-4.1 / GPT-4o-mini / Llama)  
- FastAPI microservice for real-time inference  
- Dockerized deployment  
- GitHub Actions CI/CD pipeline  
- MCP-powered automation + observability  
- Full metrics, tests, and reusable architecture  

Designed to show **strong engineering readiness** for ML Engineering internships at:  
**Netflix, Stripe, Amazon, Microsoft, NVIDIA, Meta, OpenAI.**

---

# 🧠 Key Features

### 🔹 **1. End-to-End ML Pipeline**
- Data ingestion + validation  
- Feature engineering  
- XGBoost, LightGBM, RandomForest, Logistic Regression  
- Automatic model evaluation  
- Artifact tracking  

### 🔹 **2. Real-Time Inference API (FastAPI)**
Endpoints:
- `POST /predict` → ML prediction  
- `POST /explain_llm` → LLM-based explanation  
- `POST /retrieve_context` → RAG retrieval  

### 🔹 **3. LLM Reasoning Module**
Uses:
- GPT-4.1  
- GPT-4o-mini  
- Llama 3  

Provides:
- Natural language reasoning  
- Safety-aligned explanation  
- Context-aware output  

### 🔹 **4. RAG System for Interpretability**
Using FAISS/ChromaDB:
- Retrieves relevant medical context  
- Supplies LLM explanation  
- Boosts transparency and user trust  

### 🔹 **5. MCP Tooling**
Integrated model coordination tools:
- Vector search  
- File system access  
- Model serving  
- Observability  

### 🔹 **6. Full CI/CD**
- Automated tests  
- Docker build pipeline  
- Lint + format checks  
- Secret scanning  
- Deployment-ready artifact push  

---

# 🏗️ Architecture

<p align="center">
  <img src="https://raw.githubusercontent.com/Trojan3877/asset-storage/main/diagrams/diabetes_architecture_dark.png"
       width="90%">
</p>

For full details, see **ARCHITECTURE.md**.

High-level workflow:

User Input → API → Model → Prediction
↓
RAG Engine
↓
LLM Reasoner
↓
Final JSON Output


---

# 📁 Directory Structure



Diabetes_Prediction_ML_Pipeline/
│
├── config/
├── data/
├── src/
│ ├── data_ingestion/
│ ├── data_preprocessing/
│ ├── model_training/
│ ├── model_evaluation/
│ ├── prediction_service/
│ ├── rag/
│ └── llm_explanations/
│
├── artifacts/
├── metrics/
├── tests/
├── docker/
├── .github/workflows/
│
├── ARCHITECTURE.md
├── metrics.md
├── SECURITY.md
├── requirements.txt
└── README.md


---

# ⚙️ Quick Start

### **1. Clone the repo**
```bash
git clone https://github.com/Trojan3877/Diabetes_Prediction_ML_Pipeline.git
cd Diabetes_Prediction_ML_Pipeline

2. Create environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows

3. Install dependencies
pip install -r requirements.txt

4. Initialize vector store
python src/rag/build_vector_store.py

5. Run FastAPI service
uvicorn src.prediction_service.api:app --reload


API running at:

http://localhost:8000/docs

🧪 Testing

Run all tests:

pytest -q

🐳 Docker Deployment
docker build -t diabetes-ml .
docker run -p 8000:8000 diabetes-ml

📊 Metrics

Full details in:
📄 metrics.md

Includes:

Accuracy

Precision

Recall

F1-Score

ROC-AUC

Confusion matrix

Feature importance

🔐 Security & Compliance

See SECURITY.md for:

API key handling

PII protection

Secure model serving

Input validation

Rate limiting

🤖 LLM + RAG Examples
Explain a prediction:
POST /explain_llm
{
  "inputs": {...}
}


LLM returns a safe, interpretable explanation.

Retrieve relevant medical context:
POST /retrieve_context
{
  "query": "high insulin and BMI risk"
}

⭐ Why This Project Stands Out (Internship-Level)

This repo demonstrates:

✔ Real-world ML engineering
✔ Microservice architecture
✔ RAG + LLM integration
✔ Production-grade design
✔ CI/CD automation
✔ Dockerization
✔ Testing discipline
✔ Clear documentation

This is the exact structure FAANG recruiters look for.

📬 Contact

Author: Corey Leath
GitHub: https://github.com/Trojan3877

Email: corey22blue@hotmail.com

LinkedIn: linkedin.com/in/corey-leath
