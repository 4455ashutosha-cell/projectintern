import streamlit as st

def disease_prediction():

    st.header(
        "AI Disease Predictor"
    )

    symptoms = st.text_area(
        "Enter Symptoms"
    )

    if st.button(
        "Predict"
    ):
        st.success(
            "Disease Analysis Generated"
        )

        st.write(
            "Possible Disease:"
        )

        st.write(
            "Recommended Medicines:"
        )