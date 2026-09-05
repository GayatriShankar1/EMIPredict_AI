import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(page_title="EMI Predict AI", page_icon="💳", layout="wide")

st.title("💳 EMI Eligibility & Max Capacity Predictor")
st.write("Enter financial details below to assess loan risk and recommended monthly EMI capacity.")

# Load models
@st.cache_resource
def load_models():
    clf = joblib.load('models/classifier.pkl')
    reg = joblib.load('models/regressor.pkl')
    return clf, reg

try:
    clf, reg = load_models()
except Exception as e:
    st.error("⚠️ Models not found! Ensure models/classifier.pkl and models/regressor.pkl exist.")
    st.stop()

# Layout layout columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Applicant Profile")
    age = st.number_input("Age", 18, 100, 30)
    salary = st.number_input("Monthly Salary (₹)", 10000, 1000000, 50000)
    credit_score = st.slider("Credit Score", 300, 900, 750)
    existing_emi = st.number_input("Current Monthly EMI (₹)", 0, 500000, 5000)
    bank_balance = st.number_input("Bank Balance (₹)", 0, 10000000, 100000)

with col2:
    st.subheader("📊 Expenses & Loan Request")
    rent = st.number_input("Monthly Rent (₹)", 0, 200000, 10000)
    utilities = st.number_input("Groceries & Utilities (₹)", 0, 200000, 8000)
    other_exp = st.number_input("Other Monthly Expenses (₹)", 0, 200000, 5000)
    req_amount = st.number_input("Requested Loan Amount (₹)", 10000, 10000000, 200000)
    req_tenure = st.number_input("Requested Tenure (Months)", 3, 360, 24)

# Prediction button
if st.button("🚀 Calculate Eligibility"):
    # Feature calculation matching notebook feature engineering
    total_expenses = rent + utilities + other_exp + existing_emi
    disposable = salary - total_expenses
    dti = existing_emi / salary if salary > 0 else 0
    exp_ratio = total_expenses / salary if salary > 0 else 0

    # Display results
    st.markdown("---")
    st.subheader("📌 Prediction Results")
    
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.metric("Total Monthly Expenses", f"₹{total_expenses:,.2f}")
        st.metric("Disposable Income", f"₹{disposable:,.2f}")
        
    with res_col2:
        st.metric("Debt-to-Income (DTI)", f"{dti*100:.1f}%")
        st.metric("Expense-to-Income Ratio", f"{exp_ratio*100:.1f}%")

    st.success("✅ Assessment Completed Successfully!")