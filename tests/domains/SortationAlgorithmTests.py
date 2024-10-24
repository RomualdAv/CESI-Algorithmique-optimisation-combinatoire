import unittest

from src.utils import *
from src.domains.SortationAlgorithm import boxDeliveryWindowSorting

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
if __name__ == '__main__':
    unittest.main()