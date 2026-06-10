import networkx as nx

def build_doctor_graph(df):

    G = nx.Graph()

    for _, row in df.iterrows():

        doctor = row["Doctor Name"]

        hospital = row["Hospital"]

        state = row["State"]

        G.add_node(
            doctor,
            node_type="Doctor"
        )

        G.add_node(
            hospital,
            node_type="Hospe thiital"
        )

        G.add_node(
            state,
            node_type="State"
        )

        G.add_edge(
            doctor,
            hospital
        )

        G.add_edge(
            hospital,
            state
        )

    return G