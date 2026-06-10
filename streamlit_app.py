import streamlit as st

st.set_page_config(
    page_title="SmartVet AI",
    page_icon="🐄",
    layout="wide"
)

st.markdown("""
# 🐄 SmartVet AI Ecosystem

### AI Powered Veterinary & Dairy Management Platform
""")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Animals", "4200+")

with col2:
    st.metric("Doctors", "4000+")

with col3:
    st.metric("Hospitals", "400+")

with col4:
    st.metric("Medicines", "1000+")

st.divider()

role = st.selectbox(
    "Select Login Type",
    [
        "Farmer",
        "Vet",
        "Customer"
    ]
)

phone = st.text_input(
    "Phone Number"
)

if st.button("Send OTP"):
    st.success("OTP Sent Successfully")