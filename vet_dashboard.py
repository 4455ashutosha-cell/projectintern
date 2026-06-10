import streamlit as st

def vet_dashboard():

    st.title(
        "🩺 Vet Dashboard"
    )

    col1,col2,col3 = st.columns(3)

    col1.metric(
        "Consultations",
        "120"
    )

    col2.metric(
        "Patients",
        "500"
    )

    col3.metric(
        "Prescriptions",
        "350"
    )