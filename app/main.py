# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("models/logistic_regression_model.pkl")

# Define FastAPI app
app = FastAPI(title="Disease Prediction API")

# Input data format
class InputData(BaseModel):
    age: int
    gender: int
    bmi: float
    blood_pressure: float
    glucose: float
    insulin: float
    skin_thickness: float

# Define root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Disease Prediction API!"}

# Define prediction route
@app.post("/predict")
def predict_disease(data: InputData):
    features = np.array([[data.age, data.gender, data.bmi, data.blood_pressure,
                          data.glucose, data.insulin, data.skin_thickness]])
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}
