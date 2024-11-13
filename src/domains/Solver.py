import networkx as nx
import itertools
from networkx.algorithms.shortest_paths.generic import shortest_path

def path_weight(graph, path) -> float:
    """
    Return the weight of the path
    """
    try:
        weight = 0
        index = 0
        while index < len(path)-1:
            last_edge = None
            for edge in shortest_path(graph, path[index], path[index + 1], "weight"):
                if last_edge is None:
                    last_edge = edge
                    continue
                weight += graph[last_edge][edge]["weight"]
                last_edge = edge
            index += 1
    except Exception:
        return float('inf')
    return weight

def find_shortest_tour(graph, delivery: list[int]) -> (list[int], float):
    """
    The function send you the better path
    """
    # Ajouter le sommet de départ à la fin pour fermer le circuit
    delivery = delivery + [delivery[0]]
    taboo_list = []

    # Générer toutes les permutations des sommets à visiter (sauf le sommet de départ)
    shortest_tour = []
    min_weight = float('inf')
    no_move = 0

    # Itérer sur toutes les permutations des sommets à visiter, en excluant le sommet de départ
    for perm in itertools.permutations(delivery[1:-1]):  # Exclure le sommet de départ de la permutation
        # Créer le chemin complet (départ + permutation + retour)
        path = [delivery[0]] + list(perm) + [delivery[0]]
        if path in taboo_list:
            continue
        taboo_list.append(path)
        if len(taboo_list) > 1000:
            taboo_list.pop(0)
        # Calculer le poids total de ce chemin
        weight = path_weight(graph, path)

        # Mettre à jour le chemin le plus court si le poids est plus petit
        if weight < min_weight:
            print(weight)
            min_weight = weight
            shortest_tour = path
            no_move = 0
        else:
            no_move += 1

        if no_move == 100000:
            break

    index = 0
    list_path = []
    while index < len(shortest_tour) - 1:
        for edge in shortest_path(graph, shortest_tour[index], shortest_tour[index + 1], "weight"):
            if list_path and edge == list_path[-1]:
                continue
            list_path += [edge]
        index += 1

    return list_path, min_weight

def display_text(list_path: list[int], min_weight:float)-> None:
    """
    The function display a path

    :param list_path: The path
    :param min_weight: The time to past on the path
    """
    print("Le chemin le plus court :", list_path)
    print("Poids total du chemin :", min_weight)

def matrix_to_graph(matrix: list[list[float]]):
    """
    Change a matrix into a graph
    """
    graph = nx.DiGraph()

    for i in range(len(matrix)):
        graph.add_node(i)

    i = 0
    j = 0
    while i < len(matrix):
        while j < len(matrix):
            if matrix[i][j] != float('inf'):
                graph.add_edge(i, j, weight=matrix[i][j])
            j += 1
        i+=1

    return graph