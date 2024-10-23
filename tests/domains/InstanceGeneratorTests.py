import unittest
from src.domains.InstanceGenerator import *


class TestInstanceGenerator(unittest.TestCase):

    def test_should_the_random_graph_generation(self):
        nb_nodes = 10
        nb_edges = 5
        index = 0
        old_graph = generateGraph(nb_nodes, nb_edges)
        for index in range(0, 10):
            graph = generateGraph(nb_nodes, nb_edges)
            self.assertEqual(len(graph.nodes), nb_nodes)
            self.assertEqual(len(graph.edges), nb_edges)
            self.assertNotEqual(graph.edges, old_graph.edges)
            index += 1
if __name__ == '__main__':
    unittest.main()