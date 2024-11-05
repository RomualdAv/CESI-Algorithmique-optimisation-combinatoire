from src.domains.random.GraphGenerator import *
from src.domains.random.TruckGenerator import *

def generate_instance(instance_name: str, nb_nodes: int,nb_edges: int, symmetric: bool, nb_truck: int):
    """
    Generate an instance with random values
    :param instance_name: The name of the instance
    :param nb_nodes: The number of nodes in the graph
    :param nb_edges: The number of edges in the graph
    :param symmetric: If the graph is symmetric
    :param nb_truck: The number of truck in the instance
    """
    # Generate the graph
    graph = generateGraph(nb_nodes, nb_edges, symmetric)
    # Generate the trucks
    trucks = generate_truck(nb_truck)
    for truck in trucks:
        starting_node = random.randint(0, nb_nodes-1)
        generate_box(truck,nb_nodes,starting_node)
    # Save the instance
    #TODO : CSV

def __main__():
    generate_instance("test", 10, 20, True, 2)