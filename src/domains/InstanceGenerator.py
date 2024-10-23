import networkx as nx

def generateGraph(nb_nodes: int, nb_edges: int) -> nx.Graph:
    """
    Generate a graph with nb_nodes nodes and nb_edges edges.

    Args:
        nb_nodes (int): The number of nodes in the graph.
        nb_edges (int): The number of edges in the graph.
    """
    return nx.gnm_random_graph(nb_nodes, nb_edges)