import unittest
from src.domains.random.GraphGenerator import *


class GraphGeneratorCase(unittest.TestCase):

    def test_should_generate_graph_with_correct_number_of_nodes_and_edges(self):
        nb_nodes = 10
        nb_edges = 5
        symmetric_graph = generateGraph(nb_nodes, nb_edges, True)
        asymmetric_graph = generateGraph(nb_nodes, nb_edges, False)

        # Vérifie que le nombre de nœuds est correct
        self.assertEqual(len(symmetric_graph), nb_nodes)
        self.assertEqual(len(asymmetric_graph), nb_nodes)

        # Compte le nombre d'arêtes
        edge_count = sum(1 for i in range(nb_nodes) for j in range(nb_nodes) if symmetric_graph[i][j] != float('inf'))
        self.assertEqual(edge_count, nb_edges)
        edge_count = sum(1 for i in range(nb_nodes) for j in range(nb_nodes) if asymmetric_graph[i][j] != float('inf'))
        self.assertEqual(edge_count, nb_edges)

    def test_should_generate_graph_with_symmetric_weight(self):
        nb_nodes = 20
        nb_edges = 300
        graph = generateGraph(nb_nodes, nb_edges, True)

        repetitions = 0

        # Vérifier que le poids des arêtes est symétrique
        for i in range(nb_nodes):
            for j in range(nb_nodes):
                if graph[i][j] == graph[j][i]:
                    repetitions += 1

        self.assertEqual(repetitions, 400)

    def test_should_generate_graph_with_asymmetric_weight(self):
        nb_nodes = 20
        nb_edges = 300
        graph = generateGraph(nb_nodes, nb_edges, False)

        repetitions = 0

        # Vérifier que le poids des arêtes est symétrique
        for i in range(nb_nodes):
            for j in range(nb_nodes):
                if graph[i][j] == graph[j][i]:
                    repetitions += 1

        self.assertLessEqual(repetitions, 150)

    def test_should_generate_different_graphs(self):
        nb_nodes = 10
        nb_edges = 5
        old_graph = generateGraph(nb_nodes, nb_edges, True)
        for _ in range(10000):
            graph = generateGraph(nb_nodes, nb_edges, True)
            self.assertNotEqual(graph, old_graph)
            old_graph = graph


if __name__ == '__main__':
    unittest.main()
