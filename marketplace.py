import streamlit as st

def marketplace():

    st.header(
        "Buy Dairy Products"
    )

    products = [
        "Milk",
        "Paneer",
        "Butter",
        "Ghee",
        "Cheese"
    ]

    for product in products:

        st.card = st.container()

        with st.card:

            st.subheader(
                product
            )


            st.button(
                f"Buy {product}"
            )