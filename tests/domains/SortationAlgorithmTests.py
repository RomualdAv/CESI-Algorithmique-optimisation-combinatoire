import unittest
import time

from src.utils import *
from src.domains.SortationAlgorithm import *
from src.domains.InstanceGenerator import generateGraph

class TestInstanceGenerator(unittest.TestCase):

    def test_should_the_random_graph_generation(self):
        truck = Truck("truck1", Size(10,10,10), TypeTruck.PLATED)

        dw1 = DeliveryWindow(datetime.datetime(2023,11,12,8,0), datetime.datetime(2023,11,12,9,0))
        dw2 = DeliveryWindow(datetime.datetime(2023, 11, 12, 9, 0), datetime.datetime(2023, 11, 12, 11, 0))
        dw3 = DeliveryWindow(datetime.datetime(2023, 11, 12, 12, 0), datetime.datetime(2023, 11, 12, 14, 0))
        dw4 = DeliveryWindow(datetime.datetime(2023, 11, 12, 14, 0), datetime.datetime(2023, 11, 12, 18, 0))
        dw5 = DeliveryWindow(datetime.datetime(2023, 11, 12, 8, 0), datetime.datetime(2023, 11, 12, 17, 30))

        depot1 = Depot(1,"depot1", True,dw1)
        depot2 = Depot(2, "depot1", True, dw2)
        depot3 = Depot(3, "depot1", True, dw3)
        depot4 = Depot(4, "depot1", True, dw4)
        depot5 = Depot(5, "depot1", True, dw5)

        box1 = Box(uuid.uuid4(), depot1,Size(2,2,2),TypeBox.TOXIC)
        box2 = Box(uuid.uuid4(), depot2, Size(2, 2, 2), TypeBox.TOXIC)
        box3 = Box(uuid.uuid4(), depot3, Size(2, 2, 2), TypeBox.TOXIC)
        box4 = Box(uuid.uuid4(), depot4, Size(2, 2, 2), TypeBox.TOXIC)
        box5 = Box(uuid.uuid4(), depot5, Size(2, 2, 2), TypeBox.TOXIC)

        truck.addFret(box1)
        truck.addFret(box2)
        truck.addFret(box3)
        truck.addFret(box4)
        truck.addFret(box5)

        liste_gen = boxDeliveryWindowSorting(truck)

        liste = [box1, box2, box3, box5, box4]

        self.assertEqual(liste, liste_gen)

    def test_should_generate_matrix_Floyd_Warshall_for_not_oriented_graph(self):
        graph = [
            [0, 2, 5],
            [2, 0, float('INF')],
            [5, float('INF'), 0],
        ]

        matrix = createMatrixItinerary(graph)

        matrix_manual = [
            [Itinerary(0,0,[],0), Itinerary(0,1,[],2), Itinerary(0,2,[],5)],
            [Itinerary(1,0,[],2), Itinerary(1,1,[],0), Itinerary(1,2,[0],7)],
            [Itinerary(2,0,[],5), Itinerary(2,1,[0],7), Itinerary(2,2,[],0)],
        ]

        self.assertEqual(matrix, matrix_manual)

    def test_should_generate_matrix_Floyd_Warshall_for_oriented_graph(self):
        graph = [
            [0, 2, 5,8,float('INF')],
            [2, 0, float('INF'),8,5],
            [5, float('INF'), 0,6,3],
            [8, 2, 5, 0, 3],
            [3, 2, float('INF'), 7, 0],
        ]

        matrix = createMatrixItinerary(graph)

        for i in matrix:
            for j in i:
                self.assertNotEqual(j.getTravelTime(), float('INF'))

    def test_should_generate_matrix_Floyd_Warshall_for_oriented_graph_with_negative_cycle(self):
        graph = generateGraph(1000, 850000, False)
        print("Start test performance")
        start = time.time()

        matrix = createMatrixItinerary(graph)

        end = time.time()
        print("End test performance")
        print("Time to generate matrix for 1000 nodes and 700 edges: ", end-start)
        for i in matrix:
            for j in i:
                self.assertNotEqual(j.getTravelTime(), float('INF'))
if __name__ == '__main__':
    unittest.main()