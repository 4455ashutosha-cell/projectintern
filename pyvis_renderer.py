from pyvis.network import Network

def render_graph(G):

    net = Network(
        height="800px",
        width="100%",
        bgcolor="#111111",
        font_color="white"
    )

    net.from_nx(G)

    net.save_graph(
        "graph.html"
    )

    return "graph.html"