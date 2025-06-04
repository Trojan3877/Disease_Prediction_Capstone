![Project Pipeline](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAAARCAYAAADcKkjkAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BJQ0MgUHJvZmlsZQAAKJFjYGRgYOhkYGD4T2CkYAJiMzJyMjAxQGJKsEpmtH6WhkYmRgYmB9RMvAz0DKPTi1sDL28sfBzMvMyTBiZGIj7sHEcDpAJlY2NjoCVBhYq4HWD4DAAAE3ElEQVR4nO2cW24bRRCHX2ngoDFAaM4SIuHCNOsHE5FDwATowD/A5KUxMpbyBBqKkYWQFatAxBYFIpIohDgIIg3VBbTUEJIPiKmvlsRUkF+WMx/2ztkst2dmd2Z9F/Z6bOZ6fm9+5v33OzMKXeSTpuN9jy9AMZzRM96HTCCkRvp+EG2Bl4f5TS3vOFRNI4QGWAl3I+JenCDT6FwFzV8higvQIF6W1fszFMAH0CInay4xzAHwsgYhlIP8KRuBrYAXRhN8WaAMPGwxArhUQSk8ShISrU0GTmHFiKBCC0Ebjz6z1DSc4MgrmkCAOja9KeEWYlRWYSjxA5goLMekMCZIMQPCgIsAAgSygVIGJ++hEd4ndIhYAeOKfgjQzfhCBGwkTO9aQ+wjL5RLGNXxCP4bWF5eO2LUm2iQ8ok1jER6DIpwNcOp8yMwg1vCzCA8IKhwMbtmBG51ppFTWD+8gqVxJBFPWuR0lOhxwDscZXP9ky6Wo2q5UjuMJigy1VHzk3jBW0bCX79bMh8bEjQDDKY5hgngYr9XUkXzOs3JOyycNzuJL8mkC8j6dJ0eNcxvYtwuGqcBMceJgxeC2Nin4Rx18dWmj1IZDFH0xY4T4ZcU8r/L7hAcXMFxlLeaLGCNFcFaAL3+sxuGwA/SHmDlgYdRLfNyHe069nCyBoI1jxs/n0K9NsrDKB2jrA4h5N/g7D8j7kWEHE8lpjEydk7DS9Nj+1GcBvmsZhD8+8AGuaDoElYxOEHHV/LeF8xLwL+LTECZ8B7eCdwxflkkFs8qSCOcTJpMUWdj5iwakI+wdMF40bYcIoh+VF4/EjLJBgikY5SlcIeXO0A+OOAuEE1wUvBh5gv6P8/Zw2em/hyY+pHPy51x7URjl2vkGNJtlFpQ9hE1GJ+TQA2hzsH9MZpPu0h3mH3eJKNy2hCeSc4zGDikyij1Fkwp8WPf0soYJ+CCQlLpq13I5Y/gWiONbzDQ+uar6kUZBR4E2JuAfWhE1hOYqGaEg9p5lxwFg9A1cGFKpjs5iFRjYqmYnWWNRhcUKxukCUPmSPwMDuWjyQ43OV1wlX1YUf4lEmYThKMUNsZE+V02Kc2ruFbbDmuriY8W7oeTXR7hc0S4whcPkUXojTHjxKeER1uOaWprREzaPLsTOFs8lR0NHm4XSz8iC0jags0bRk0VPk26MqElkc27dl7352OiurJz66D28jyz+pi265dk9bb+PqEGAxJA6vxL9UyYn5sfc08AY4nxQgLmEKjpHHre63xBjyJ5CT7lNqGB+uPc7Yb5TBpYRE3EHi+PI0efirsbhCNa8kGxYSzyOYdQzJ5PwZBhpiWRjPVMiIzGZDumYDF+0GDdYxfubMRspevBHgYs8R8RHEM4ww8qdtpehB7tMzjyjFgUgiT8ROHOq2Q1fSHqELLG3dv09oU0N)


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
