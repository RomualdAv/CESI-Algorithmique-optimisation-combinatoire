import random

def generateGraph(nb_nodes: int, nb_edges: int) -> list[list[float]]:
    """
    Generate a graph with nb_nodes nodes and nb_edges edges.
    This graph is represented by an adjacency matrix.
    The weight of the edges represent the time to go from one node to another, if the time is infinite, you don't have a direct edge.

    Args:
        nb_nodes (int): The number of nodes in the graph.
        nb_edges (int): The number of edges in the graph.

    Returns:
        list[list[float]]: The generated graph as an adjacency matrix.
    """
    # Create a graph with nb_nodes nodes and no edges
    graph = [[float('inf')] * nb_nodes for _ in range(nb_nodes)]

    # Add randomly nb_edges edges to the graph
    for _ in range(nb_edges):
        # Get randomly two nodes
        node1 = random.randint(0, nb_nodes - 1)
        node2 = random.randint(0, nb_nodes - 1)
        # Make sure the two nodes are different
        while node1 == node2:
            node1 = random.randint(0, nb_nodes - 1)
            node2 = random.randint(0, nb_nodes - 1)
        # Generate a random weight for the edge
        prob = random.randint(0, 100)
        # 70% of the time, the weight is between 1 and 180 because it's a small way
        if prob < 70:
            weight = random.randint(1, 180)
        else:
            weight = random.randint(181, 360)
        # Add the edge to the graph
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph