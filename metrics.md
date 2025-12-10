
Diabetes_Prediction_Capstone/metrics.md


# 📄 **metrics.md — Diabetes Prediction Model Evaluation**

## 🧪 **Model Performance Summary**

The table below summarizes the performance of each model trained during the pipeline execution.
All results are computed dynamically during each training run using the test dataset.

| Model               | Accuracy              | Precision  | Recall     | F1 Score   | ROC-AUC    |
| ------------------- | --------------------- | ---------- | ---------- | ---------- | ---------- |
| Logistic Regression | *computed at runtime* | *computed* | *computed* | *computed* | *computed* |
| Random Forest       | *computed at runtime* | *computed* | *computed* | *computed* | *computed* |
| XGBoost             | *computed at runtime* | *computed* | *computed* | *computed* | *computed* |
| LightGBM            | *computed at runtime* | *computed* | *computed* | *computed* | *computed* |

> The system automatically selects the **best model based on ROC-AUC**, a gold-standard metric for medical binary classification tasks.

---

 **Best Model Selected**

During the latest training run, the system selected:

```
Best Model: <determined at runtime>
ROC-AUC: <value>
```

The chosen model is automatically saved to:

```
src/models/model.pkl
```

Additional saved model formats:

* `xgb_model.json` (XGBoost native format)
* `lgbm_model.txt` (LightGBM native format)

---

**Confusion Matrix**

The confusion matrix structure used for evaluation:

```
[[TN, FP],
 [FN, TP]]
```

Where:

* **TN**: True Negative
* **FP**: False Positive
* **FN**: False Negative
* **TP**: True Positive

This matrix is produced automatically in `evaluate.py`.

---

## ⚙️ **Hyperparameters Used**

### **Logistic Regression**

* `C = 1.0`
* `max_iter = 200`

### **Random Forest**

* `n_estimators = 200`
* `max_depth = 10`
* `random_state = 42`

### **XGBoost**

* `n_estimators = 250`
* `learning_rate = 0.05`
* `max_depth = 6`
* `subsample = 0.8`
* `colsample_bytree = 0.8`

### **LightGBM**

* `num_leaves = 31`
* `learning_rate = 0.05`
* `n_estimators = 200`

 **Feature Engineering Summary**

The system enhances the raw dataset with medically-informed engineered features:

* **BMI_Risk** — categorical risk bucket
* **Glucose × BMI Interaction** — high-value clinical predictor
* **Insulin Resistance Proxy (IR_Proxy)** — HOMA-IR approximation
* **Age_Group** — medically relevant age bins
* **Polynomial Features** — optional via config for higher-order interactions

These engineered features significantly improve predictive performance and interpretability.

**RAG + LLM Evaluation**

The system incorporates **Retrieval-Augmented Generation (RAG)** to support prediction explanations.

Capabilities include:

* FAISS vector search
* Semantic embeddings (OpenAI or Sentence Transformers)
* GPT-4o-mini–based medical explanations
* Top-K retrieval from medical reference documents

This hybrid ML + LLM design increases transparency and reliability for clinical use cases.

 **Future Enhancements**

Planned upgrades for next versions:

* **SHAP explainability** for better clinical transparency
* **Model ensembling** to boost predictive performance
* **Kubernetes + Helm deployment** for scalable environments
* **Grafana / Prometheus dashboards** for real-time monitoring
* **Expanded RAG corpus** (CDC, NIH, peer-reviewed research)



