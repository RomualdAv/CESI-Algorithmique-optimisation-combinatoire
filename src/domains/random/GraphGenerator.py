import random

def generateGraph(nb_nodes: int, nb_edges: int, symmetric: bool) -> list[list[float]]:
    """
    Generate a graph with nb_nodes nodes and nb_edges edges.
    This graph is represented by an adjacency matrix.
    The weight of the edges represent the time to go from one node to another, if the time is infinite, you don't have a direct edge.

    Args:
        nb_nodes (int): The number of nodes in the graph.
        nb_edges (int): The number of edges in the graph.
        symmetric (bool): If the graph is symmetric or not.
    Returns:
        list[list[float]]: The generated graph as an adjacency matrix.
    """
    # Create a graph with nb_nodes nodes and no edges
    graph = [[float('inf')] * nb_nodes for _ in range(nb_nodes)]
    # Create the list of this edges
    list_edges = []
    start = 1
    for i in range(nb_nodes):
        for j in range(start, nb_nodes):
            list_edges.append((i, j))
        start += 1

    # Add randomly nb_edges edges to the graph
    index = 0
    while index < nb_edges:
        # Get randomly two nodes
        node1, node2 = list_edges.pop(random.randint(0, len(list_edges) - 1))
        # Generate a random weight for the edge
        if nb_edges-index != 1:
            if symmetric:
                generateSymmetricWeight(graph, node1, node2)
            else:
                generateAsymmetricWeight(graph, node1, node2)
            index += 2
        else:
            if IsSmallWay():
                graph[node1][node2] = GetSmallWay()
            else:
                graph[node1][node2] = GetLongWay()
            index += 1

    return graph

def generateSymmetricWeight(graph: list[list[float]], node1: int, node2: int) -> None:
    """
    Generate a symmetric weight for the graph.

    Args:
        graph (list[list[float]]): The graph to modify.
        node1 (int): The first node.
        node2 (int): The second node.
    """
    if IsSmallWay():
        weight = GetSmallWay()
    else:
        weight = GetLongWay()
    # Add the edge to the graph
    graph[node1][node2] = weight
    graph[node2][node1] = weight

def generateAsymmetricWeight(graph: list[list[float]], node1: int, node2: int) -> None:
    """
    Generate an asymmetric weight for the graph.

    Args:
        graph (list[list[float]]): The graph to modify.
        node1 (int): The first node.
        node2 (int): The second node.
    """
    if IsSmallWay():
        graph[node1][node2] = GetSmallWay()
        graph[node2][node1] = GetSmallWay()
    else:
        graph[node1][node2] = GetLongWay()
        graph[node2][node1] = GetLongWay()

def IsSmallWay() -> bool:
    """
    Generate a random boolean to know if the way is small or not.

    Returns:
        bool: True if the way is small, False otherwise.
    """
    return random.randint(0, 100) < 70

def GetSmallWay() -> int:
    """
    Generate a random integer for a small way.

    Returns:
        int: The generated integer.
    """
    return random.randint(1, 180)

def GetLongWay() -> int:
    """
    Generate a random integer for a big way.

    Returns:
        int: The generated integer.
    """
    return random.randint(181, 360)