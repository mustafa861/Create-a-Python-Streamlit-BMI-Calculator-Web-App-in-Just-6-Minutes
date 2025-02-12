import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.lider("Enter your height (in cm):",100, 250, 175)
weight = st.slider("Enter your weight (in cm):",40, 200, 70)