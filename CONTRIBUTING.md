# 🤝 Contributing Guide — Diabetes Prediction System

Thank you for your interest in contributing to this project!  
This guide outlines best practices, workflow standards, and expectations for external or future contributors.

This repository follows **professional ML engineering standards**, including modular architecture, CI/CD, testing, security, and documentation.

---

# 📌 Code of Conduct

By contributing, you agree to:

- Write clean, readable, well-documented code  
- Follow Python best practices (PEP8)  
- Respect other contributors  
- Test code before submitting  
- Not commit secrets or sensitive information  

This project follows a zero-tolerance policy toward harassment, discrimination, or harmful behavior.

---

# 🧠 Project Overview

This project is a **production-ready ML pipeline and API** integrating:

- FastAPI  
- XGBoost, LightGBM, Random Forest, Logistic Regression  
- RAG (FAISS vector search + OpenAI embeddings)  
- LLM medical explanations  
- Docker deployment  
- GitHub Actions CI/CD  

See `README.md` for full system architecture.

---

# 🌱 How to Contribute

## 1. Fork the Repository

## 2. Clone Your Fork
```bash
git clone https://github.com/<your-username>/Diabetes_Prediction_Capstone
cd Diabetes_Prediction_Capstone
git checkout -b feature/add-shap-explainability
git checkout -b fix/api-response-schema
git checkout -b docs/update-readme
🧪 Testing Requirements

Before submitting a PR, run:

Linting
black .
flake8 .

Tests
pytest -q

Build Docker locally
docker build -t diabetes-api .


If any of the above fail, fix the issue before submitting.

🧬 Code Standards
Python

Follow PEP8

Use type hints

Keep functions small and single-purpose

Add docstrings to all modules, classes, and functions

FastAPI

Use Pydantic models for validation

Return standardized JSON responses

Add meaningful error messages

ML Code

No hard-coded paths

No magic numbers

Log model performance

Keep training and inference completely separate

RAG Code

Test retrieval step independently

Avoid embedding the same document multiple times

🔐 Security Guidelines

Do NOT commit:

.env

API keys

model weights

raw patient-like data

FAISS indexes

These are protected by .gitignore.

📦 Pull Request Guidelines
PR Format:
Title: feat: add LIME explainability module

Description:
- Added new explainability module for model interpretation
- Updated README
- Added tests for new functionality

Checklist:
- [x] Linting passed
- [x] Tests added/passed
- [x] CI/CD pipeline succeeded

PR Requirements:

✔ Clear description
✔ Clean diff (no unnecessary formatting)
✔ Tests included if applicable
✔ CI/CD must pass
✔ No secrets committed

🏁 Commit Convention (Recommended)

Follow the Angular-style convention:

feat: add new model for hyperparameter search
fix: correct FastAPI endpoint validation
docs: update metrics documentation
test: add missing unit tests
refactor: simplify preprocessing pipeline
ci: update GitHub Actions workflow
chore: update dependencies

🧭 Roadmap (Areas Open for Contribution)

Add SHAP visualization support

Add calibration curve API endpoint

Add K-fold cross-validation training option

Expand RAG corpus with more medical papers

Add model registry support (MLflow)

Add monitoring dashboards (Grafana / Prometheus)

Build Streamlit UI for patient-friendly predictions

🎉 Thank You for Contributing!

Your contributions help improve this system and demonstrate high-quality ML engineering practices.
For questions, open an Issue or contact: https://github.com/Trojan3877
