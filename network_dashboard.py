import streamlit as st

def network_dashboard():

    st.title(
        "🕸 Disease Knowledge Graph"
    )

    st.info(
        "NetworkX Visualization Here"
    )

    menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Farmer",
        "Vet",
        "Customer",
        "Analytics",
        "Knowledge Graph"
    ]
)