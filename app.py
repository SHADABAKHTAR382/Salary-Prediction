import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction App")

st.divider()
st.write("With this app,you can get estmations for the salaries of the company employees")
years=st.number_input("Enter the years of company",value=1.0,step=0.1,min_value=0.0)
X=[years]
model=joblib.load("linearmodel.pkl")
st.divider()
predict=st.button("Press the button for salary prediction")

if predict:
    st.balloons()
    X1=np.array([X])
    prediction=model.predict(X1)
    st.write(f"Salary prediction is{prediction}")