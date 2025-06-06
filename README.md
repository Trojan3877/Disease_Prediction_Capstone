![MIT License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub repo stars](https://img.shields.io/github/stars/Trojan3877/Diabetes-Prediction-Capstone-Project?style=social)
![GitHub forks](https://img.shields.io/github/forks/Trojan3877/Diabetes-Prediction-Capstone-Project?style=social)
![Build passing](https://img.shields.io/github/actions/workflow/status/Trojan3877/Diabetes-Prediction-Capstone-Project/ci.yml?branch=main)
![Python version](https://img.shields.io/badge/python-3.9%2B-blue)




![image](https://github.com/user-attachments/assets/ffc83026-f2b0-4653-a4eb-814ad54750b5)



# Disease_Prediction_Capstone
PIMA Indian Diabetes Dataset
# Disease Prediction Capstone

## Project Overview
The **Disease Prediction Capstone** project aims to build a robust machine learning pipeline to predict the onset of diabetes using the PIMA Indian Diabetes Dataset. The focus is on creating modular, well-commented code that follows best practices in machine learning engineering and ensuring comprehensive evaluation with quantifiable metrics and visualizations. 

## Repository Structure
```
Disease_Prediction_Capstone/
│
├── data/
│   ├── raw/            # Raw dataset files (e.g., CSV)
│   └── processed/      # Preprocessed data ready for modeling
│
├── notebooks/
│   ├── 01_EDA.ipynb    # Exploratory Data Analysis
│   └── 02_Model_Training.ipynb  # Model training and evaluation
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
│
├── models/
│   ├── trained_model.pkl  # Serialized trained model
│
├── results/
│   ├── roc_curve.png
│   ├── confusion_matrix.png
│   └── feature_importance.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd Disease_Prediction_Capstone
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset:**
   - The PIMA Indian Diabetes dataset can be downloaded from:
     - Kaggle: https://www.kaggle.com/uciml/pima-indians-diabetes-database
     - UCI
