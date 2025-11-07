import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏦 Loan Amount Prediction App")

st.write("This app predicts the **loan amount** that could be approved based on applicant details.")

# Collect user inputs
st.subheader("📋 Enter Applicant Details")

applicant_income = st.number_input("Applicant Income ($)", min_value=0, value=60000)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=721)
employment_years = st.number_input("Years of Employment", min_value=0, value=1)
debt_to_income_ratio = st.number_input("Debt-to-Income Ratio (%)", min_value=0.0, value=15.5)
loan_term = st.number_input("Loan Term (years)", min_value=1, value=25)

# Predict when button clicked
if st.button("🔮 Predict Loan Amount"):
    input_df = pd.DataFrame([{
        "Applicant_Income": applicant_income,
        "Credit_Score": credit_score,
        "Employment_Years": employment_years,
        "Debt_to_Income_Ratio": debt_to_income_ratio,
        "Loan_Term": loan_term
    }])

    prediction = model.predict(input_df)[0][0]
    st.success(f"💰 Predicted Loan Amount Approved: **${prediction:,.2f}**")
