import unittest
from src.domains.SolutionChecker import *
from src.utils import *


class SolutionCheckerTests(unittest.TestCase):
    def test_should_check_containable_when_all_is_good(self):
        depot = Depot(1,"depot")

        list_boxes = [
            Box(uuid.uuid4(),depot,Size(10,10,10),TypeBox.NOTSPECIFY),
            Box(uuid.uuid4(), depot, Size(20, 20, 10), TypeBox.TOXIC),
            Box(uuid.uuid4(), depot, Size(10, 10, 10), TypeBox.ALIMENTAL),
            Box(uuid.uuid4(), depot, Size(10, 30, 10), TypeBox.CORROSIVE),
            Box(uuid.uuid4(), depot, Size(10, 10, 10), TypeBox.CORROSIVE),
            Box(uuid.uuid4(), depot, Size(50, 10, 10), TypeBox.NOTSPECIFY),
        ]
        list_truck = [
            Truck("The beast", Size(30, 10, 25), TypeTruck.WATERTIGHT),
            Truck("The beast", Size(40, 10, 20), TypeTruck.WATERTIGHT),
        ]

        self.assertTrue(is_containable(list_boxes,list_truck))

    def test_should_check_containable_when_you_have_too_many_boxes(self):
        depot = Depot(1,"depot")

        list_boxes = [
            Box(uuid.uuid4(),depot,Size(10,10,10),TypeBox.NOTSPECIFY),
            Box(uuid.uuid4(), depot, Size(20, 20, 10), TypeBox.TOXIC),
            Box(uuid.uuid4(), depot, Size(10, 10, 10), TypeBox.ALIMENTAL),
            Box(uuid.uuid4(), depot, Size(10, 30, 10), TypeBox.CORROSIVE),
            Box(uuid.uuid4(), depot, Size(10, 10, 10), TypeBox.CORROSIVE),
            Box(uuid.uuid4(), depot, Size(50, 10, 10), TypeBox.NOTSPECIFY),
        ]
        list_truck = [
            Truck("The beast", Size(5, 10, 10), TypeTruck.WATERTIGHT),
            Truck("The beast", Size(20, 10, 20), TypeTruck.WATERTIGHT),
        ]

        self.assertFalse(is_containable(list_boxes,list_truck))

    def test_should_check_reachability_when_all_is_good(self):
        depot1 = Depot(0,"depot")
        depot2 = Depot(1, "depot")
        depot3 = Depot(2, "depot")

        graph = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        list_boxes = [
            Box(uuid.uuid4(),depot1,Size(10,10,10),TypeBox.NOTSPECIFY),
            Box(uuid.uuid4(), depot2, Size(20, 20, 10), TypeBox.TOXIC),
            Box(uuid.uuid4(), depot3, Size(10, 10, 10), TypeBox.ALIMENTAL),
        ]

        self.assertTrue(is_reachable(list_boxes,graph))

    def test_should_check_reachability_when_we_cant_reach_vertex(self):
        depot1 = Depot(0,"depot")
        depot2 = Depot(1, "depot")
        depot3 = Depot(3, "depot")

        graph = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        list_boxes = [
            Box(uuid.uuid4(),depot1,Size(10,10,10),TypeBox.NOTSPECIFY),
            Box(uuid.uuid4(), depot2, Size(20, 20, 10), TypeBox.TOXIC),
            Box(uuid.uuid4(), depot3, Size(10, 10, 10), TypeBox.ALIMENTAL),
        ]

        self.assertFalse(is_reachable(list_boxes,graph))

    def test_should_check_solvable_when_all_is_good(self):
        depot1 = Depot(0,"depot1")
        depot2 = Depot(1, "depot2")
        depot3 = Depot(2, "depot3")

        graph = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        list_boxes = [
            Box(uuid.uuid4(),depot1,Size(1,2,2),TypeBox.NOTSPECIFY),
            Box(uuid.uuid4(), depot2, Size(3, 4, 1.5), TypeBox.TOXIC),
            Box(uuid.uuid4(), depot3, Size(20, 5, 5), TypeBox.ALIMENTAL),
        ]
        list_truck = [
            Truck("The beast", Size(7, 4, 15), TypeTruck.WATERTIGHT),
            Truck("The beast", Size(30, 15, 25), TypeTruck.WATERTIGHT),
        ]

        self.assertTrue(is_solvable(list_truck,list_boxes,graph))

    def test_should_check_solvable_when_size_boxes_is_too_much(self):
        depot1 = Depot(0,"depot1")
        depot2 = Depot(1, "depot2")
        depot3 = Depot(2, "depot3")

        graph = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        list_boxes = [
            Box(uuid.uuid4(),depot1,Size(1,40,2),TypeBox.NOTSPECIFY),
            Box(uuid.uuid4(), depot2, Size(30, 4, 48), TypeBox.TOXIC),
            Box(uuid.uuid4(), depot3, Size(20, 5, 5), TypeBox.ALIMENTAL),
        ]
        list_truck = [
            Truck("The beast", Size(7, 4, 4), TypeTruck.WATERTIGHT),
            Truck("The beast", Size(20, 7, 10), TypeTruck.WATERTIGHT),
        ]

        with self.assertRaises(InstanceError):
            self.assertTrue(is_solvable(list_truck,list_boxes,graph))

    def test_should_check_solvable_when_one_box_is_not_reachable(self):
        depot1 = Depot(0,"depot1")
        depot2 = Depot(1, "depot2")
        depot3 = Depot(7, "depot3")

        graph = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        list_boxes = [
            Box(uuid.uuid4(),depot1,Size(1,2,2),TypeBox.NOTSPECIFY),
            Box(uuid.uuid4(), depot2, Size(3, 4, 1.5), TypeBox.TOXIC),
            Box(uuid.uuid4(), depot3, Size(20, 5, 5), TypeBox.ALIMENTAL),
        ]
        list_truck = [
            Truck("The beast", Size(7, 4, 15), TypeTruck.WATERTIGHT),
            Truck("The beast", Size(30, 15, 25), TypeTruck.WATERTIGHT),
        ]

        with self.assertRaises(InstanceError):
            self.assertTrue(is_solvable(list_truck, list_boxes, graph))

    def test_should_check_solvable_when_you_forgot_data(self):
        depot1 = Depot(0,"depot1")
        depot2 = Depot(1, "depot2")
        depot3 = Depot(2, "depot3")

        graph = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        list_boxes = [
            Box(uuid.uuid4(),depot1,Size(1,2,2),TypeBox.NOTSPECIFY),
            Box(uuid.uuid4(), depot2, Size(3, 4, 1.5), TypeBox.TOXIC),
            Box(uuid.uuid4(), depot3, Size(20, 5, 5), TypeBox.ALIMENTAL),
        ]
        list_truck = [
            Truck("The beast", Size(7, 4, 15), TypeTruck.WATERTIGHT),
            Truck("The beast", Size(30, 15, 25), TypeTruck.WATERTIGHT),
        ]

        with self.assertRaises(InstanceError):
            self.assertTrue(is_solvable([], list_boxes, graph))

        with self.assertRaises(InstanceError):
            self.assertTrue(is_solvable(list_truck, [], graph))

        with self.assertRaises(InstanceError):
            self.assertTrue(is_solvable(list_truck, list_boxes, []))
if __name__ == '__main__':
    unittest.main()
