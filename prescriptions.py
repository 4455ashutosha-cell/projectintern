import streamlit as st

def prescriptions():

    st.header(
        "Prescription"
    )

    disease = st.text_input(
        "Disease"
    )

    medicine = st.text_input(
        "Medicine"
    )

    dosage = st.text_input(
        "Dosage"
    )

    withdrawal = st.number_input(
        "Withdrawal Period"
    )

    if st.button(
        "Generate Prescription"
    ):
        st.success(
            "Prescription Generated"
        )