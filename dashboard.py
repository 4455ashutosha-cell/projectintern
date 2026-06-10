import streamlit as st
import pandas as pd

from analytics.animal_analytics import *
from analytics.disease_analytics import *
from analytics.medicine_analytics import *
from analytics.doctor_analytics import *
from analytics.milk_analytics import *

def analytics_dashboard():

    st.title("📊 SmartVet Analytics")

    animal_df = pd.read_excel(
        "data/Animal_Dairy_Dataset_4200.xlsx"
    )

    medicine_df = pd.read_excel(
        "data/Veterinary_Medicines_Master.xlsx"
    )

    disease_df = pd.read_excel(
        "data/Veterinary_Disease_Warehouse_Project.xlsx"
    )

    doctor_df = pd.read_excel(
        "data/Synthetic_India_Vet_Database_400_Hospitals_4000_Doctors.xlsx"
    )

    st.subheader(
        "Animal Analytics"
    )

    st.plotly_chart(
        species_distribution(animal_df),
        use_container_width=True
    )

    st.plotly_chart(
        breed_distribution(animal_df),
        use_container_width=True
    )

    st.subheader(
        "Disease Analytics"
    )

    st.plotly_chart(
        disease_frequency(disease_df),
        use_container_width=True
    )

    st.plotly_chart(
        mortality_analysis(disease_df),
        use_container_width=True
    )

    st.subheader(
        "Medicine Analytics"
    )

    st.plotly_chart(
        medicine_cost_analysis(medicine_df),
        use_container_width=True
    )

    st.plotly_chart(
        withdrawal_analysis(medicine_df),
        use_container_width=True
    )

    st.subheader(
        "Doctor Analytics"
    )

    st.plotly_chart(
        specialization_chart(doctor_df),
        use_container_width=True
    )

    st.plotly_chart(
        state_doctors(doctor_df),
        use_container_width=True
    )

    st.subheader(
        "Milk Analytics"
    )

    st.plotly_chart(
        milk_production(animal_df),
        use_container_width=True
    )

    st.plotly_chart(
        milk_distribution(animal_df),
        use_container_width=True
    )

    px.choropleth()
    px.treemap()
    px.sunburst()
    px.scatter_matrix()
    px.timeline()
    px.funnel()
