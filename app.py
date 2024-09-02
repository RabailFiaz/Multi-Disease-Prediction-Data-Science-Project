import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the trained models
heart_disease_model = pickle.load(open("C:\\Users\\HP\\Desktop\\HDP-BD\\saved models\\heart_disease_model.sav", 'rb'))
diabetes_model = pickle.load(open("C:\\Users\\HP\\Desktop\\Multi-DP\\saved models\\Diabetes_model.sav", 'rb'))
parkinsons_model = pickle.load(open("C:\\Users\\HP\\Desktop\\Multi-DP\\saved models\\parkinsons_model.sav", 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction",
        ["Diabetes Prediction System", "Heart Disease Prediction", "Parkinson's Prediction"],
        icons=["activity", "heart", "person"],
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f9f9f9"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "2px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )

# Diabetes Prediction System
if selected == "Diabetes Prediction System":
    st.title("Diabetes Prediction using ML")

    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=110)
    blood_pressure = st.number_input("Blood Pressure Level", min_value=0, max_value=122, value=70)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=99, value=20)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=846, value=79)
    bmi = st.number_input("BMI", min_value=0.0, max_value=67.1, value=32.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.42, value=0.3725)
    age = st.number_input("Age", min_value=0, max_value=120, value=33)

    if st.button("Diabetes Test Result"):
        features = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]
        diab_prediction = diabetes_model.predict(features)
        if diab_prediction[0] == 1:
            st.success("The person is suffering from Diabetes")
        else:
            st.success("The person is not suffering from Diabetes")

# Heart Disease Prediction
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=200, value=120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG Result", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", min_value=50, max_value=220, value=150)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels Colored by Flouroscopy", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia", [0, 1, 2], format_func=lambda x: "Normal" if x == 0 else "Fixed Defect" if x == 1 else "Reversible Defect")

    if st.button("Heart Test Result"):
        features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        heart_prediction = heart_disease_model.predict(features)
        if heart_prediction[0] == 1:
            st.success("The person is suffering from heart disease")
        else:
            st.success("The person is not suffering from heart disease")

# Parkinson's Prediction
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0)
    fhi = st.number_input("MDVP:Fhi(Hz)", min_value=0.0)
    flo = st.number_input("MDVP:Flo(Hz)", min_value=0.0)
    jitter_percent = st.number_input("MDVP:Jitter(%)", min_value=0.0)
    jitter_abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0)
    rap = st.number_input("MDVP:RAP", min_value=0.0)
    ppq = st.number_input("MDVP:PPQ", min_value=0.0)
    ddp = st.number_input("Jitter:DDP", min_value=0.0)
    shimmer = st.number_input("MDVP:Shimmer", min_value=0.0)
    shimmer_db = st.number_input("MDVP:Shimmer(dB)", min_value=0.0)
    apq3 = st.number_input("Shimmer:APQ3", min_value=0.0)
    apq5 = st.number_input("Shimmer:APQ5", min_value=0.0)
    apq = st.number_input("MDVP:APQ", min_value=0.0)
    dda = st.number_input("Shimmer:DDA", min_value=0.0)
    nhr = st.number_input("NHR", min_value=0.0)
    hnr = st.number_input("HNR", min_value=0.0)
    rpde = st.number_input("RPDE", min_value=0.0)
    dfa = st.number_input("DFA", min_value=0.0)
    spread1 = st.number_input("spread1", min_value=-7.0)
    spread2 = st.number_input("spread2", min_value=0.0)
    d2 = st.number_input("D2", min_value=0.0)
    ppe = st.number_input("PPE", min_value=0.0)

    if st.button("Parkinson's Test Result"):
        features = [[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]]
        parkinsons_prediction = parkinsons_model.predict(features)
        if parkinsons_prediction[0] == 1:
            st.success("The person is suffering from Parkinson's disease")
        else:
            st.success("The person is not suffering from Parkinson's disease")
