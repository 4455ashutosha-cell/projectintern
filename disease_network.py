import networkx as nx
import pandas as pd

def build_disease_graph(df):

    G = nx.Graph()

    for _, row in df.iterrows():

        disease = row["Disease"]

        symptoms = str(
            row["Symptoms"]
        ).split(",")

        G.add_node(
            disease,
            node_type="Disease"
        )

        for symptom in symptoms:

            symptom = symptom.strip()

            G.add_node(
                symptom,
                node_type="Symptom"
            )

            G.add_edge(
                disease,
                symptom
            )

    return G 