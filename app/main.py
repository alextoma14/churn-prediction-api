import joblib
import pandas as pd
from fastapi import FastAPI

from app.schemas import Customer

app = FastAPI()

model = joblib.load("models/xg.pkl")


@app.get("/")
def root():
    return {"message": "Churn Prediction API"}


@app.post("/predict")
def predict(input: Customer):
    frame = pd.DataFrame([input.model_dump()])
    print(frame.dtypes)
    print(frame.head())
    score = model.predict_proba(frame)

    return {"churn_probability": float(score[0][1])}
