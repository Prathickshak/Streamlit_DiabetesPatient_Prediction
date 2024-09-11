import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('diabeties_saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

classifier_loaded = data["model"]
standardizer = data["x"]

def show_predicted_page():
    st.title("Diabeties patient Prediction")

    st.write("""### We need some information to predict the Diabeties""")

    Pregnancies_col, Glucose_col, Blood_Pressure_col = st.columns(3)
    SkinThickness_col, Insulin_col, bmi_col = st.columns(3)
    Diabetes_Pedigree_Fuction_col, Age_col = st.columns(2)

    Pregnancies = Pregnancies_col.number_input("No. of Pregnancies:", min_value=0, value=0)
    Glucose = Glucose_col.number_input("Glucose Level:", min_value=0, value=0)
    Blood_Pressure = Blood_Pressure_col.number_input("Blood Pressure:", min_value=0, value=0)
    SkinThickness = SkinThickness_col.number_input("Skin Thickness:", min_value=0, value=0)
    Insulin = Insulin_col.number_input("Insulin Level:", min_value=0, value=0)
    bmi = bmi_col.number_input("BMI:", min_value=0.0, value=0.0)
    Diabetes_Pedigree_Fuction = Diabetes_Pedigree_Fuction_col.number_input("Diabetes Pedigree Function:", min_value=0.0, value=0.0)
    Age = Age_col.number_input("Age:", min_value=0, value=0)

    ok = st.button("Predict")

    if ok:
        X = np.asarray([[Pregnancies,Glucose,Blood_Pressure,SkinThickness,Insulin,bmi,Diabetes_Pedigree_Fuction,Age]])
        x_reshaped = X.reshape(1,-1)
        x_std = standardizer.transform(x_reshaped)


        prediction = classifier_loaded.predict(x_std)
        
        if (prediction[0]==0):
            st.success("The person have not diabetic")
        else:
            st.warning("The person have diabetic")
        