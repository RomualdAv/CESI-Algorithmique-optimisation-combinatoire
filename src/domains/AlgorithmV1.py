import numpy as np

def floyd_warshall(matrice):
    n = len(matrice)
    dist = np.array(matrice)
    
    # Appliquer l'algorithme de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def shortest_path_floyd(dist, start, end):
    return dist[start][end]

def itineraire_glouton(matrice, start, mandatory):
    n = len(matrice)
    
    # Étape 1 : Calculer les distances les plus courtes entre toutes les paires de nœuds
    dist = floyd_warshall(matrice)
    
    # Étape 2 : Ajouter le point de départ à la liste des nœuds à visiter
    nodes_to_visit = [start] + mandatory
    total_distance = 0
    path = [start]
    current_node = start
    
    # Étape 3 : Visiter les nœuds obligatoires
    while nodes_to_visit:
        # Trouver le nœud le plus proche parmi ceux qui restent à visiter
        min_distance = float('inf')
        next_node = None
        
        for node in nodes_to_visit:
            if node != current_node:
                distance = dist[current_node][node]
                if distance < min_distance:
                    min_distance = distance
                    next_node = node
        
        # Ajouter le nœud visité au chemin
        total_distance += min_distance
        path.append(next_node)
        current_node = next_node
        nodes_to_visit.remove(next_node)
    
    # Retourner au point de départ
    total_distance += dist[current_node][start]
    path.append(start)
    
    return path, total_distance