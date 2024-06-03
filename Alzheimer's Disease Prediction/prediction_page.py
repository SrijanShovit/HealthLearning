import pandas as pd
import streamlit as st

# Constants for Categories
ETHNICITY_CATEGORIES = ['Hisp/Latino', 'Not Hisp/Latino', 'Unknown']
IMPUTED_CATEGORIES = ['True', 'False']
PTRACCAT_CATEGORIES = ['Asian', 'Black', 'White']
PTGENDER_CATEGORIES = ['Female', 'Male']
APOE4_CATEGORIES = ['0', '1', '2']
MODEL_FILE_PATH = 'model/alzheimer_model.pkl'

class Conditions:
    AD = "AD"
    LMCI = "LMCI"
    CN = "CN"

abbreviation = {
    Conditions.AD: "Alzheimer's Disease",
    Conditions.LMCI: "Late Mild Cognitive Impairment",
    Conditions.CN: "Cognitively Normal"
}

def convert_to_one_hot(selected_category, all_categories):
    return [True if category == selected_category else False for category in all_categories]

def predict_condition(input_data):
    try:
        loaded_model = joblib.load(MODEL_FILE_PATH)
        predictions = loaded_model.predict(input_data)
        return predictions
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return

def prediction_page():
    st.title("Patient Information")

    age = st.number_input("Age", min_value=0, max_value=122, step=1, value=65)
    gender = st.selectbox("Gender", ("Male", "Female"))
    education = st.number_input("Years of Education", min_value=0, value=12)

    st.write("<br>", unsafe_allow_html=True)

    st.header("Demographics")
    ethnicity = st.radio("Ethnicity", list(ETHNICITY_OPTIONS.keys()))
    race_cat = st.radio("Race Category", PTRACCAT_CATEGORIES)

    st.write("<br>", unsafe_allow_html=True)

    st.header("Genetic Information")
    apoe_allele_type = st.selectbox("APOE Allele Type", APOE4_CATEGORIES)
    apoe_genotype = st.selectbox("APOE4 Genotype", ["2,2", "2,3", "2,4", "3,3", "3,4", "4,4"])
    imputed_genotype = st.radio("Imputed Genotype", IMPTED_CATEGORIES)

    st.header("Cognitive Assessment")
    mmse = st.number_input("MMSE Score", min_value=0, max_value=30, step=1)

    predict_button = st.button("Predict")
    st.write("")

    if age and education and mmse and apoe_genotype and race_cat and gender and apoe_allele_type and imputed_genotype and ethnicity and predict_button:
        st.write("Thank you for entering the patient's information.")
        progress_text = "Please wait, we're predicting your clinical condition..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)

        user_input = [age, education, mmse]
        user_input += convert_to_one_hot("PTRACCAT_" + race_cat, PTRACCAT_CATEGORIES)
        user_input += convert_to_one_hot("APOE Genotype_" + apoe_genotype, APOE_CATEGORIES)
        user_input += convert_to_one_hot("PTETHCAT_" + ethnicity, ETHNICITY_CATEGORIES)
        user_input += convert_to_one_hot("APOE4_" + apoe_allele_type, APOE4_CATEGORIES)
        user_input += convert_to_one_hot("PTGENDER_" + gender, PTGENDER_CATEGORIES)
        user_input += convert_to_one_hot("imputed_genotype_" + imputed_genotype, IMPTED_CATEGORIES)

        data = pd.DataFrame([user_input])
        predicted_condition = predict_condition(data)

        st.write("")
        st.write("")
        st.subheader("Predicted Clinical Condition:")
        st.write(f"**{predicted_condition[0]}** ({abbreviation[predicted_condition[0]]})")
        st.subheader("Condition Description:")
        st.write(condition_description[predicted_condition[0]])
