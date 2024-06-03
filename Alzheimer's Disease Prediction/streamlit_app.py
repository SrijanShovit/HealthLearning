import streamlit as st
from prediction_page import prediction_page

st.set_page_config(
    page_title="Alzheimer's Prediction System",
    page_icon=":brain:",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.image("assets/side_banner.png")

st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Prediction"],
)

st.sidebar.write("""
# Disclaimer
The predictions provided by this system are for informational purposes only. Consult a healthcare professional for accurate diagnosis and advice.

# About Me
This application is developed by [arpy8](https://github.com/arpy8).

# Contact
For inquiries, please contact me at [arpitsengar99@gmail.com](mailto:arpitsengar99@gmail.com).
""")

if __name__ == "__main__":

    if app_mode == "Home":
        st.title("Welcome to the Alzheimer's Prediction System")

        st.image("assets/banner.png")

        st.write("""
            ## About Alzheimer's Disease
            Alzheimer's disease (AD) is a progressive neurodegenerative disease. Though best known for its role in declining memory function, symptoms also include: difficulty thinking and reasoning, making judgements and decisions, and planning and performing familiar tasks. It may also cause alterations in personality and behavior. The cause of AD is not well understood. There is thought to be a significant hereditary component. For example, a variation of the APOE gene, APOE e4, increases risk of Alzheimer's disease.

            ## Purpose of the project
            The purpose of this project proposal is to develop a machine learning model for the early prediction of Alzheimer's disease. Alzheimer's disease is a devastating neurodegenerative disorder that affects millions of individuals worldwide. Early detection is crucial for better patient care and the development of potential interventions. This project aims to leverage machine learning techniques to create a predictive model that can identify individuals at risk of Alzheimer's disease based on relevant data.
            """)

    if app_mode == "Prediction":
        prediction_page()
