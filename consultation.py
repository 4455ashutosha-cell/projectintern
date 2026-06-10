import streamlit as st

def consultation():

    st.header(
        "Consultation"
    )

    animal = st.text_input(
        "Animal ID"
    )

    notes = st.text_area(
        "Consultation Notes"
    )

    if st.button(
        "Save"
    ):
        st.success(
            "Consultation Saved"
        )
        