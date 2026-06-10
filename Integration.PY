import streamlit as st
import pandas as pd

from network_graphs.disease_network import *
from network_graphs.pyvis_renderer import *

def show_graph():

    df = pd.read_excel(
        "data/Veterinary_Disease_Warehouse_Project.xlsx"
    )

    G = build_disease_graph(
        df
    )

    render_graph(G)

    HtmlFile = open(
        "graph.html",
        "r",
        encoding="utf-8"
    )

    source = HtmlFile.read()

    st.components.v1.html(
        source,
        height=800
    )