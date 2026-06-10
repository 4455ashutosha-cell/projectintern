import networkx as nx

def build_knowledge_graph(
    disease_df,
    medicine_df,
    doctor_df
):

    G = nx.Graph()

    for _, row in disease_df.iterrows():

        disease = row["Disease"]

        medicine = row["Medicine"]

        G.add_node(
            disease,
            node_type="Disease"
        )

        G.add_node(
            medicine,
            node_type="Medicine"
        )

        G.add_edge(
            disease,
            medicine
        )

    for _, row in doctor_df.iterrows():

        doctor = row["Doctor Name"]

        specialization = row[
            "Specialization"
        ]

        G.add_node(
            doctor,
            node_type="Doctor"
        )

        G.add_node(
            specialization,
            node_type="Specialization"
        )

        G.add_edge(
            doctor,
            specialization
        )

    return G