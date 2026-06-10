import streamlit as st

def farmer_dashboard():

    st.title(
        "👨‍🌾 Farmer Dashboard"
    )

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "My Animals",
        "25"
    )

    col2.metric(
        "Vaccinated",
        "20"
    )

    col3.metric(
        "Active Cases",
        "2"
    )

    col4.metric(
        "Milk Yield",
        "550 L"
    )