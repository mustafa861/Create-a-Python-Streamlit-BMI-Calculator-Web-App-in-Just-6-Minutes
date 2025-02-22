import streamlit as st
import pandas as pd

st.set_page_config(page_title="BMI Calculator", layout="wide")
st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in cm):",40, 200, 70)