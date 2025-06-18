# predict.py
"""
FastAPI endpoint to make disease predictions based on trained ML model.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/disease_model.pkl")

# Define expected input schema
class PatientData(BaseModel):
    age: int
    bmi: float
    blood_pressure: float
    cholesterol: float
    glucose: float

# Initialize FastAPI app
app = FastAPI(title="Disease Prediction API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Disease Prediction API"}

@app.post("/predict")
def predict_disease(data: PatientData):
    try:
        df = pd.DataFrame([data.dict()])
        prediction = model.predict(df)
        result = "Positive" if prediction[0] == 1 else "Negative"
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
