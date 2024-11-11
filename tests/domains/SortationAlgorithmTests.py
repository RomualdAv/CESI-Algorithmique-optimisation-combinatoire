import unittest
from src.domains.SortationAlgorithm import *
from src.utils.Box import *
from src.utils.Truck import *

class SortationAlgorithmTests(unittest.TestCase):

    def setUp(self):
        # Create some mock boxes and trucks for testing
        depot1 = Depot(0, "Depot 0")
        depot2 = Depot(1, "Depot 1")
        depot3 = Depot(2, "Depot 2")
        self.box1 = Box(uuid.uuid4(), depot1, Size(1,1,1), TypeBox.ALIMENTAL)
        self.box2 = Box(uuid.uuid4(), depot2, Size(2,2,2), TypeBox.NOTSPECIFY)
        self.box3 = Box(uuid.uuid4(), depot1, Size(1.5,1.5,1.5), TypeBox.FRAGILE)
        self.box4 = Box(uuid.uuid4(), depot1, Size(1, 1.5, 0.5), TypeBox.ALIMENTAL)
        self.box5 = Box(uuid.uuid4(), depot3, Size(0.6, 1, 0.6), TypeBox.CORROSIVE)
        self.box6 = Box(uuid.uuid4(), depot3, Size(0.6, 1, 0.6), TypeBox.CORROSIVE)
        self.box7 = Box(uuid.uuid4(), depot3, Size(0.6, 1, 0.6), TypeBox.CORROSIVE)
        self.truck1 = Truck("Truck1", Size(3,3,6), TypeTruck.REFRIGERATE)
        self.truck2 = Truck("Truck2", Size(2,2,4), TypeTruck.OPEN)
        self.truck3 = Truck("Truck3", Size(1, 1, 1), TypeTruck.PLATED)
        self.truck4 = Truck("Truck4", Size(3, 3, 8), TypeTruck.WATERTIGHT)
        self.graph = [[0, 1, 1],
                      [1, 0, 0],
                      [1, 0, 0]]

    def test_sort_by_type(self):
        algorithm = SortationAlgorithm([self.box1, self.box2, self.box3, self.box4,self.box5,self.box6,self.box7], [self.truck1, self.truck2], self.graph)
        sorted_boxes = algorithm._SortationAlgorithm__sortByType()
        # Check if the boxes are sorted by type
        self.assertGreater(len(sorted_boxes), 0)
        self.assertIn("ALIMENTAL", sorted_boxes)
        self.assertIn("NOTSPECIFY", sorted_boxes)
        self.assertIn("FRAGILE", sorted_boxes)
        self.assertIn("CORROSIVE", sorted_boxes)

        self.assertEqual(len(sorted_boxes["ALIMENTAL"]), 2)
        self.assertEqual(len(sorted_boxes["NOTSPECIFY"]), 1)
        self.assertEqual(len(sorted_boxes["FRAGILE"]), 1)
        self.assertEqual(len(sorted_boxes["CORROSIVE"]), 3)

    def test_check_containability(self):
        instance1 = SortationAlgorithm([self.box1, self.box2, self.box3], [self.truck1, self.truck2], self.graph)
        instance2 = SortationAlgorithm([self.box2, self.box3], [self.truck2], self.graph)

        self.assertTrue(instance1._SortationAlgorithm__checkContainability())
        self.assertTrue(instance2._SortationAlgorithm__checkContainability())

    def test_check_containability_failure(self):
        algorithm = SortationAlgorithm([self.box1, self.box6], [self.truck1], self.graph)

        with self.assertRaises(InstanceError):
            algorithm._SortationAlgorithm__checkContainability()

    def test_get_truck_loaded(self):
        algorithm = SortationAlgorithm([self.box1, self.box2, self.box3, self.box4,self.box5,self.box6,self.box7], [self.truck1, self.truck4], self.graph)

        loaded_trucks = algorithm.getTruckLoaded()
        self.assertGreater(len(loaded_trucks), 0)
        self.assertTrue(all(truck.get_current_weight() > 0 for truck in loaded_trucks))
        self.assertEqual(sum(len(truck.get_fret()) for truck in loaded_trucks),7)

if __name__ == '__main__':
    unittest.main()