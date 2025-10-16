import streamlit as st
import pandas as pd
import pickle


# Load Train Model
with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)


# Take Inputs from user
online_class_taken = st.selectbox("Online Class Taken ?", ['Yes','No'])
study_hours_week = st.number_input("Study Hours per week", min_value=0, max_value=100)
study_hours = st.number_input("Study Hours per Day", min_value=0, max_value=100)
attandence_perc = st.number_input("Attandence %", min_value = 0, max_value = 100)
attandence = st.number_input("Attandence Rate", min_value = 0, max_value = 100)
prev_grade = st.number_input("Previous Grade", min_value = 0, max_value = 100)
ExtracurricularActivities = st.number_input("Extracurricular Activities D/h", min_value = 0, max_value = 100)

# Convert inputs to numeric (same encoding as training)

online_class_taken = 1 if online_class_taken=="Yes" else 0


#  Create input dataframe

input_data = pd.DataFrame([[online_class_taken, study_hours, attandence, study_hours_week, attandence_perc, prev_grade, ExtracurricularActivities]])

# Predict button

if st.button("predict"):
    pred = model.predict(input_data)[0]
    st.write("Predection: ", "pass" if pred==1 else "Fail")
