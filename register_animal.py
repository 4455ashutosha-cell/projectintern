import streamlit as st

def register_animal():

    st.header(
        "Register New Animal"
    )

    animal_name = st.text_input(
        "Animal Name"
    )

    species = st.selectbox(
        "Species",
        [
            "Cow",
            "Buffalo",
            "Goat",
            "Sheep"
        ]
    )

    breed = st.text_input(
        "Breed"
    )

    age = st.number_input(
        "Age"
    )

    weight = st.number_input(
        "Weight"
    )

    vaccination = st.selectbox(
        "Vaccination Status",
        ["Yes","No"]
    )

    if st.button(
        "Register Animal"
    ):
        st.success(
            "Animal Registered Successfully"
        )