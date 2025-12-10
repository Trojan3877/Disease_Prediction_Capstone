# 🧠 Model Card — Diabetes Prediction System

## 📌 Overview
This model predicts the likelihood of Type 2 Diabetes using structured clinical and biometric data from the Pima Indians Diabetes Dataset and extended engineered features.  
It supports clinical decision-assistance and educational use cases, NOT standalone medical diagnosis.

---

# 📚 Intended Use

### ✔ Appropriate Use Cases
- Clinical decision support *with a licensed medical professional involved*
- Early risk screening tools
- Patient education dashboards
- Research and academic ML experimentation
- Feature analysis and exploratory modeling

### ❌ NOT Intended For
- Providing medical diagnosis without oversight
- Emergency medical decision-making
- High-risk clinical settings where false positives/negatives cause direct harm
- Use on populations not represented in the training dataset

---

# 🧩 Model Architecture

Several models were trained:

| Model | Training Framework | Notes |
|-------|--------------------|-------|
| Logistic Regression | scikit-learn | Baseline & interpretable |
| Random Forest | scikit-learn | Nonlinear pattern detection |
| XGBoost | xgboost | High-performance boosting |
| LightGBM | lightgbm | Fast gradient boosting |

The system selects the **best model** based on **ROC-AUC** and stores it in `src/models/model.pkl`.

---

# 🧪 Evaluation Summary

Metrics computed on held-out test set:

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **ROC-AUC**
- **Confusion matrix**

See `metrics.md` for full results.

### Strengths
- High ROC-AUC performance  
- Works well for binary risk classification  
- Handles nonlinear relationships via boosted trees  
- Feature engineering improves sensitivity

### Limitations
- Dataset relatively small  
- May not generalize to all ethnicities or demographics  
- Imbalanced classes require careful threshold selection  
- Not calibrated for real medical risk scoring

---

# 📊 Dataset Description

### Source  
Pima Indians Diabetes Dataset (UCI Repository)

### Features
- Clinical metrics (Glucose, BloodPressure, BMI, Age, Insulin)
- Engineered features:
  - BMI Risk Category  
  - Age Groups  
  - Insulin Resistance Proxy (IR_Proxy)  
  - Interaction Terms (BMI × Glucose, etc.)

### Known Data Biases
- Represents a specific population group  
- Not fully representative of global diabetic risk factors  
- Contains measurement noise and missing values  
- Some features (e.g., Insulin) may have inaccuracies

---

# ⚖️ Ethical Considerations

### Potential Risks
- False negatives may give false reassurance  
- False positives may cause unnecessary anxiety  
- Model does not capture socioeconomic, genetic, or lifestyle factors  
- Dataset demographic bias may lead to unequal performance across groups

### Mitigations
- Use alongside human medical evaluation  
- Threshold tuning for different populations  
- Provide risk explanation via RAG + LLM module  
- Include uncertainty estimations where possible

---

# 🧠 Explainability & RAG Integration

The system includes:

- SHAP-style feature importance (for tree models)
- RAG pipeline for contextual medical explanations using:
  - FAISS vector DB
  - OpenAI embeddings
  - GPT-4o-mini reasoning

### Purpose
To ensure clinical transparency and support informed decision-making.

---

# 📦 Model Storage & Versioning

| Artifact | Location |
|----------|----------|
| Best model (pickle) | `src/models/model.pkl` |
| XGBoost model | `src/models/xgb_model.json` |
| LightGBM model | `src/models/lgbm_model.txt` |
| Metrics | `metrics.md` |
| CI/CD version tags | GitHub Actions (timestamp-based) |

Each new training run produces a new version.  
CI/CD pipeline supports **automatic Docker image versioning**.

---

# 🔐 Safety & Security

### Safeguards
- Sensitive keys stored in `.env` (not committed)
- MCP validation protects against malformed inputs  
- LLM explanation layer includes medical disclaimers  
- API enforces schema validation to avoid injection attacks

### PHI / HIPAA Considerations
This project is **not** designed to store personally identifiable medical data.  
For real-world deployment, implement:

- Encrypted databases  
- IAM access control  
- Audit logging  

---

# 📝 Limitations of This Model Card

This model card covers:
- Model scope  
- Ethical considerations  
- Bias  
- Evaluation  
- Intended use  

It does **not** substitute real clinical approval, FDA review, or HIPAA compliance.

---

# 📬 Contact / Ownership

**Developer:** Corey Leath  
**Repository:** https://github.com/Trojan3877/Diabetes_Prediction_Capstone  
**Purpose:** Educational + ML Engineer Career Portfolio

