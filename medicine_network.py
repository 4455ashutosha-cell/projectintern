import networkx as nx

def build_medicine_graph(df):

    G = nx.Graph()

    for _, row in df.iterrows():

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

    return G