# 📊 Model Evaluation Metrics — Diabetes Prediction System

This document summarizes all evaluation metrics, diagnostic plots, and interpretability components used to assess the Diabetes Prediction ML models.

The system evaluates 4 trained models:
- Logistic Regression  
- Random Forest  
- XGBoost  
- LightGBM  

The **best model is selected based on ROC-AUC**, a gold-standard metric for medical classification tasks.

---

# 🧮 1. Dataset Summary

The dataset used is the **Pima Indians Diabetes Dataset** with engineered clinical features.

| Statistic | Value |
|----------|-------|
| Total Samples | 768 |
| Positive Class (Outcome = 1) | ~35% |
| Negative Class (Outcome = 0) | ~65% |
| Feature Count (after engineering) | 12–18 depending on config |

⚠ **Important:**  
This dataset is moderately imbalanced, so accuracy alone is **not reliable**.  
ROC-AUC, Precision, and Recall are more meaningful.

---

# 🏆 2. Performance Summary Table

All results are generated at runtime and logged to the console automatically.

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|-------|----------|-----------|--------|----------|----------|
| Logistic Regression | *computed at runtime* | *computed* | *computed* | *computed* | *computed* |
| Random Forest | *computed* | *computed* | *computed* | *computed* | *computed* |
| XGBoost | *computed* | *computed* | *computed* | *computed* | *computed* |
| LightGBM | *computed* | *computed* | *computed* | *computed* | *computed* |

The best model is saved to:

---

# 🔁 3. Confusion Matrix Structure

Each model produces a confusion matrix of the form:

Where:
- **TN**: True Negative  
- **FP**: False Positive  
- **FN**: False Negative  
- **TP**: True Positive  

In medical ML problems, **false negatives (FN)** are the highest risk.

---

# 📈 4. ROC Curve

The ROC curve visualizes the trade-off between True Positive Rate and False Positive Rate.

The ROC-AUC score summarizes overall predictive power:

- **0.5** = random guessing  
- **0.7–0.8** = good  
- **0.8–0.9** = very good  
- **> 0.9** = excellent (rare for medical datasets)

Generated in the notebook:

```python
fpr, tpr, thresholds = roc_curve(y_test, proba_test)
roc_auc = auc(fpr, tpr)




