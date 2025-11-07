import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(page_title="Loan Prediction App", layout="centered")

st.title("🏦 Loan Amount Prediction App")

st.write("Checking model file path...")

# Debug check
model_path = os.path.abspath("../model/model.pkl")
st.write(f"🔍 Looking for model at: `{model_path}`")

# Load model safely
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    st.success("✅ Model loaded successfully!")
except FileNotFoundError:
    st.error("❌ Model file not found! Please run `train_model.py` first.")
    st.stop()
except Exception as e:
    st.error(f"⚠️ Error loading model: {e}")
    st.stop()
