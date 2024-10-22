import datetime
import sys
import unittest
sys.path.insert(0, '../src')
from src.utils.DeliveryWindow import DeliveryWindow
from src.utils.Depot import Depot
from uuid import uuid4
from src.utils.Size import Size
from src.utils.TypeTruck import TypeTruck
from src.utils.TypeBox import TypeBox
from src.utils.Box import Box
from src.utils.error import TruckError, BoxIDError
from src.utils.Truck import Truck

class TestTruck(unittest.TestCase):

    def setUp(self):
        self.size = Size(100,100,100)
        self.truck_type = TypeTruck.PLATED
        self.truck = Truck("Truck 1", self.size, self.truck_type)
        self.box1 = Box(uuid4(), Depot(1,"Lidl",True,DeliveryWindow(datetime.time,datetime.time)),Size(10,10,10),TypeBox.FRAGILE)
        self.box2 = Box(uuid4(), Depot(2,"Test",False,DeliveryWindow(datetime.time,datetime.time)),Size(20,20,20),TypeBox.ALIMENTAL)

    def test_get_name(self):
        self.assertEqual(self.truck.get_name(), "Truck 1")

    def test_get_size(self):
        self.assertEqual(self.truck.get_size(), self.size)

    def test_get_type(self):
        self.assertEqual(self.truck.get_type(), self.truck_type)

    def test_get_current_weight_empty(self):
        with self.assertRaises(TruckError):
            self.truck.getCurrentWeight()

    def test_get_current_weight(self):
        self.truck.addFret([self.box1])
        self.assertEqual(self.truck.getCurrentWeight(), 10)

    def test_can_contain(self):
        self.truck.addFret([self.box1])
        self.assertTrue(self.truck.canContain(self.box2))

    def test_is_full(self):
        self.truck.addFret([Box(uuid4(), Size(100,100,100),TypeBox.ALIMENTAL)])
        self.assertTrue(self.truck.isFull())

    def test_convey_box(self):
        self.truck.addFret([self.box1])
        self.truck.conveyBox(self.box1.getIdBox())
        with self.assertRaises(TruckError):
            self.truck.getCurrentWeight()

    def test_convey_box_not_found(self):
        with self.assertRaises(BoxIDError):
            self.truck.conveyBox(uuid4())

    def test_add_fret(self):
        self.truck.addFret([self.box1, self.box2])
        self.assertEqual(self.truck.getCurrentWeight(), 30)

    def test_add_fret_already_set(self):
        self.truck.addFret([self.box1])
        with self.assertRaises(TruckError):
            self.truck.addFret([self.box2])

if __name__ == '__main__':
    unittest.main()