import unittest
from src.domains.InstanceGenerator import generateGraph


class TestInstanceGenerator(unittest.TestCase):

    def test_should_generate_graph_with_correct_number_of_nodes_and_edges(self):
        nb_nodes = 10
        nb_edges = 5
        graph = generateGraph(nb_nodes, nb_edges)

        # Vérifie que le nombre de nœuds est correct
        self.assertEqual(len(graph), nb_nodes)

        # Compte le nombre d'arêtes
        edge_count = sum(1 for i in range(nb_nodes) for j in range(nb_nodes) if graph[i][j] != float('inf'))
        self.assertEqual(edge_count // 2, nb_edges)  # Divisé par 2 car le graphe est non orienté

    def test_should_generate_different_graphs(self):
        nb_nodes = 10
        nb_edges = 5
        old_graph = generateGraph(nb_nodes, nb_edges)
        for _ in range(10):
            graph = generateGraph(nb_nodes, nb_edges)
            self.assertNotEqual(graph, old_graph)
            old_graph = graph


if __name__ == '__main__':
    unittest.main()