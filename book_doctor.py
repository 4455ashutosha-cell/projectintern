import streamlit as st
import pandas as pd

def book_doctor():

    st.header(
        "Book Vet Doctor"
    )

    state = st.text_input(
        "State"
    )

    district = st.text_input(
        "District"
    )

    if st.button(
        "Search Doctor"
    ):
        st.success(
            "Doctors Found"
        )