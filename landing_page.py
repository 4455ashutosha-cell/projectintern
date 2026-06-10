import streamlit as st

def show_home():

    st.image(
        "assets/cattle_banner.jpg",
        use_container_width=True
    )

    st.title(
        "SmartVet AI"
    )

    st.subheader(
        "Complete Animal Healthcare Ecosystem"
    )

    st.info(
        "AI Disease Detection + Vet Consultation + Dairy Marketplace"
    )