import streamlit as st
import joblib
st.header("Salary Predictor using Linear regression")
st.caption("This ML model was designed with a sample data obtained from kaggle. Linear Regression was the algorithm used here.")

model=joblib.load('lr_model')

years=st.slider("Enter the number of years of experience",min_value=0.0,max_value=13.0,value=4.5,step=0.1)
