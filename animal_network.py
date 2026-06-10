import networkx as nx

def build_animal_graph(df):

    G = nx.Graph()

    for _, row in df.iterrows():

        animal = row["Animal_Tag_ID"]

        disease = row[
            "Disease_History"
        ]

        G.add_node(
            animal,
            node_type="Animal"
        )

        G.add_node(
            disease,
            node_type="Disease"
        )

        G.add_edge(
            animal,
            disease
        )

    return G