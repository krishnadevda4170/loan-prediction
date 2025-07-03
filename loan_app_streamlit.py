import streamlit as st
import numpy as np
import pickle

try:
    with open('model/loan_prediction.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"🚨 Error loading model: {e}")
    st.stop()

# Streamlit UI
st.set_page_config(page_title="Loan Prediction", layout="centered")
st.title("🏦 Loan Approval Prediction App")

with st.form("loan_form"):
    st.subheader("📋 Fill Applicant Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        Gender = st.selectbox("Gender", ["Female", "Male"])
        Married = st.selectbox("Married", ["No", "Yes"])
        Education = st.selectbox("Education", ["Graduate", "Not Graduate"])

    with col2:
        ApplicantIncome = st.number_input("Applicant Income", min_value=0.0)
        CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0.0)
        LoanAmount = st.number_input("Loan Amount", min_value=0.0)

    with col3:
        Loan_Amount_Term = st.number_input("Loan Term (in days)", min_value=0.0)
        Credit_History = st.selectbox("Credit History", ["Bad", "Good"])
        Property_Area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

    submitted = st.form_submit_button("Predict")

if submitted:
    # Convert inputs
    Gender = 1 if Gender == "Male" else 0
    Married = 1 if Married == "Yes" else 0
    Education = 1 if Education == "Not Graduate" else 0
    Credit_History = 1 if Credit_History == "Good" else 0

    # One-hot encoding for Property Area (use only 2 dummy vars to avoid trap)
    Property_Area_Rural = 1 if Property_Area == "Rural" else 0
    Property_Area_Semiurban = 1 if Property_Area == "Semiurban" else 0
    # Urban is assumed when both above are 0

    # Final input (10 features)
    input_features = [
        Gender,
        Married,
        Education,
        ApplicantIncome,
        CoapplicantIncome,
        LoanAmount,
        Loan_Amount_Term,
        Credit_History,
        Property_Area_Rural,
        Property_Area_Semiurban
    ]

    input_array = np.array([input_features])
    prediction = model.predict(input_array)

    if prediction[0] == 1:
        st.success("✅ Your loan is likely to be approved!")
    else:
        st.error("❌ Sorry, your loan may not be approved.")
