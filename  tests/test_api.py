from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_predict():

    response = client.post(
        "/predict",
        json={
            "gender": 0.0,
            "SeniorCitizen": 0.0,
            "Partner": 1.0,
            "Dependents": 0.0,
            "tenure": 1.0,
            "PhoneService": 0.0,
            "PaperlessBilling": 1.0,
            "MonthlyCharges": 29.85,
            "TotalCharges": 29.85,
            "MultipleLines_No": 0.0,
            "MultipleLines_No_phone_service": 1.0,
            "MultipleLines_Yes": 0.0,
            "InternetService_DSL": 1.0,
            "InternetService_Fiber_optic": 0.0,
            "InternetService_No": 0.0,
            "OnlineSecurity_No": 1.0,
            "OnlineSecurity_No_internet_service": 0.0,
            "OnlineSecurity_Yes": 0.0,
            "OnlineBackup_No": 0.0,
            "OnlineBackup_No_internet_service": 0.0,
            "OnlineBackup_Yes": 1.0,
            "DeviceProtection_No": 1.0,
            "DeviceProtection_No_internet_service": 0.0,
            "DeviceProtection_Yes": 0.0,
            "TechSupport_No": 1.0,
            "TechSupport_No_internet_service": 0.0,
            "TechSupport_Yes": 0.0,
            "StreamingTV_No": 1.0,
            "StreamingTV_No_internet_service": 0.0,
            "StreamingTV_Yes": 0.0,
            "StreamingMovies_No": 1.0,
            "StreamingMovies_No_internet_service": 0.0,
            "StreamingMovies_Yes": 0.0,
            "Contract_Month_to_month": 1.0,
            "Contract_One_year": 0.0,
            "Contract_Two_year": 0.0,
            "PaymentMethod_Bank_transfer_automatic": 0.0,
            "PaymentMethod_Credit_card_automatic": 0.0,
            "PaymentMethod_Electronic_check": 1.0,
            "PaymentMethod_Mailed_check": 0.0,
        },
    )
    assert response.status_code == 200
    assert "churn_probability" in response.json()
