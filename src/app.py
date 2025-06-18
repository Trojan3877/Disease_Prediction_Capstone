# src/app.py
"""
FastAPI app for real-time disease prediction using a trained ML model.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from src.config import MODEL_DIR

# Load model
model = joblib.load(f"{MODEL_DIR}/random_forest_model.pkl")

# Define request schema
class PatientData(BaseModel):
    features: list  # List of input features for prediction

# Initialize FastAPI app
app = FastAPI(
    title="Disease Prediction API",
    description="Real-time prediction API using Random Forest",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "Disease Prediction API is live."}

@app.post("/predict")
def predict_disease(data: PatientData):
    prediction = model.predict([np.array(data.features)])
    return {"prediction": int(prediction[0])}
