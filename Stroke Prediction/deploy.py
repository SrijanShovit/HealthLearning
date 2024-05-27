import streamlit as st
import joblib
import os
import random

# Directory to load the models
model_dir = "saved_models"

# Load the models
lrClassifier = joblib.load(os.path.join(model_dir, 'logistic_regression_model.pkl'))
nbClassifier = joblib.load(os.path.join(model_dir, 'naive_bayes_model.pkl'))

# Function to make predictions
def make_prediction(features):
    predictions = {
        "Logistic Regression": lrClassifier.predict([features])[0],
        "Naive Bayes": nbClassifier.predict([features])[0],
    }
    return predictions

# List of healthy life quotes
healthy_life_quotes = [
    "Eat a balanced diet.",
    "Exercise regularly.",
    "Get enough sleep.",
    "Stay hydrated.",
    "Practice mindfulness.",
    "Avoid smoking.",
    "Limit alcohol intake.",
    "Maintain a healthy weight.",
    "Stay socially connected.",
    "Get regular medical check-ups."
]

# Initialize session state for theme
if 'theme' not in st.session_state:
    st.session_state['theme'] = 'light'

# Function to toggle theme
def toggle_theme():
    if st.session_state['theme'] == 'light':
        st.session_state['theme'] = 'dark'
    else:
        st.session_state['theme'] = 'light'

# Apply CSS based on the theme
if st.session_state['theme'] == 'light':
    page_bg_img = '''
    <style>
    .stApp {
        background: rgba(255, 255, 255, 0.8);
        color: #000000;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    '''
else:
    page_bg_img = '''
    <style>
    .stApp {
        background: rgba(0, 0, 0, 0.7);
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    '''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar inputs
st.sidebar.title('Prediction Details')

gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
age = st.sidebar.slider('Age', 0, 100)
glucose_level = st.sidebar.slider('Glucose Level', 0, 300)
bmi = st.sidebar.slider('BMI (Body Mass Index)', 18, 30)
hypertension = st.sidebar.radio('Hypertension', ("Yes", "No"))
heart_disease = st.sidebar.radio('Heart Disease', ("Yes", "No"))
work_type = st.sidebar.radio('Work Type', ('Private', 'Self Employed', 'Government job', 'Children', 'Never Worked'))

# Map inputs to features
gender_map = {'Male': 0, 'Female': 1}
hypertension_map = {'Yes': 1, 'No': 0}
heart_disease_map = {'Yes': 1, 'No': 0}
work_type_map = {'Private': 0, 'Self Employed': 1, 'Government job': 2, 'Children': 3, 'Never Worked': 4}

features = [
    gender_map[gender],
    age,
    hypertension_map[hypertension],
    heart_disease_map[heart_disease],
    work_type_map[work_type],
    glucose_level,
    bmi
]

# Main page title and header
st.title("Brain Stroke Prediction Tool")
st.header("Input Parameters")

# Theme toggle button
if st.sidebar.button('Toggle Theme'):
    toggle_theme()

# Predict button
if st.button('Predict'):
    predictions = make_prediction(features)
    st.subheader("Predictions")
    for model, prediction in predictions.items():
        st.write(f"{model}: {'Stroke' if prediction == 1 else 'No Stroke'}")

# Button for healthy life quotes
if st.button('Get Healthy Life Quote'):
    quote = random.choice(healthy_life_quotes)
    st.subheader("Healthy Life Quote")
    st.write(quote)
