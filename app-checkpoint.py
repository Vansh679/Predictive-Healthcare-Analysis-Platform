import streamlit as st
import joblib
import numpy as np

# Load the brain and tools
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Advanced Diabetes AI", layout="wide")
st.title("🩺 Comprehensive Diabetes Risk AI")
st.write("This AI uses the BRFSS dataset to analyze risk based on 21 health indicators.")

# Create columns for a cleaner layout
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Physical Health")
    high_bp = st.selectbox("High Blood Pressure?", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    high_chol = st.selectbox("High Cholesterol?", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
    chol_check = st.selectbox("Cholesterol Check in 5 years?", [0, 1], index=1)
    bmi = st.number_input("BMI (Body Mass Index)", value=25.0)
    stroke = st.selectbox("Ever had a Stroke?", [0, 1])
    heart_disease = st.selectbox("Heart Disease or Attack?", [0, 1])

with col2:
    st.header("Lifestyle")
    smoker = st.selectbox("Smoker?", [0, 1])
    phys_activity = st.selectbox("Physical Activity in last 30 days?", [0, 1], index=1)
    fruits = st.selectbox("Eat Fruits daily?", [0, 1], index=1)
    veggies = st.selectbox("Eat Veggies daily?", [0, 1], index=1)
    alcohol = st.selectbox("Heavy Alcohol Consumption?", [0, 1])
    diff_walk = st.selectbox("Difficulty Walking/Climbing?", [0, 1])

with col3:
    st.header("Demographics & Other")
    gen_health = st.slider("General Health (1=Excellent, 5=Poor)", 1, 5, 2)
    ment_health = st.number_input("Days of poor mental health (last 30 days)", 0, 30, 0)
    phys_health = st.number_input("Days of poor physical health (last 30 days)", 0, 30, 0)
    sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Male" if x==1 else "Female")
    age = st.slider("Age Category (1=18-24, 13=80+)", 1, 13, 5)
    income = st.slider("Income Level (1=Low, 8=High)", 1, 8, 5)
    # Adding hidden constants for indicators not in form for simplicity
    any_hc, no_doc, edu = 1, 0, 5 

if st.button("Calculate My Risk"):
    # Must follow the exact column order of the CSV
    data = np.array([[high_bp, high_chol, chol_check, bmi, smoker, stroke, heart_disease, 
                      phys_activity, fruits, veggies, alcohol, any_hc, no_doc, 
                      gen_health, ment_health, phys_health, diff_walk, sex, age, edu, income]])
    
    scaled_data = scaler.transform(data)
    prediction = model.predict(scaled_data)
    prob = model.predict_proba(scaled_data)[0][1]
    
    st.divider()
    if prediction[0] == 1:
        st.error(f"### High Risk: {prob*100:.1f}% probability of Diabetes/Prediabetes.")
    else:
        st.success(f"### Low Risk: {(1-prob)*100:.1f}% probability of being Healthy.")