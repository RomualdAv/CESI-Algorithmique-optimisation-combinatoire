import unittest
from uuid import uuid4
from src.utils.Depot import Depot
from src.utils.Size import Size
from src.utils.TypeBox import *
from src.utils.Box import Box
from src.utils.error import BoxIDError
from src.utils.Truck import Truck

class TestTruck(unittest.TestCase):

    def setUp(self):
        self.size = Size(100,100,100)
        self.truck_type = TypeTruck.PLATED
        self.truck = Truck("Truck 1", self.size, self.truck_type)
        self.depot1 = Depot(1,"Lidl")
        self.depot2 = Depot(2,"Test")
        self.box1 = Box(uuid4(), self.depot1,Size(10,10,10),TypeBox.FRAGILE)
        self.box2 = Box(uuid4(), self.depot2,Size(20,20,20),TypeBox.ALIMENTAL)

    def test_get_name_when_all_is_good(self):
        self.assertEqual(self.truck.get_name(), "Truck 1")

    def test_get_size_when_all_is_good(self):
        self.assertEqual(self.truck.get_size(), self.size)

    def test_get_type_when_all_is_good(self):
        self.assertEqual(self.truck.get_type(), self.truck_type)

    def test_get_current_weight_when_you_have_add_one_box(self):
        self.truck.addFret(self.box1)
        self.assertEqual(self.truck.getCurrentWeight(), 1000)
        self.truck.conveyBox(self.box1.getIdBox())

    def test_fret_contain_box1_when_its_in(self):
        self.truck.addFret(self.box1)
        self.assertTrue(self.truck.canContain(self.box1))
        self.truck.conveyBox(self.box1.getIdBox())

    def test_truck_is_full_when_its_full(self):
        uuid = uuid4()
        self.truck.addFret(Box(uuid,self.depot1, Size(100,100,100),TypeBox.ALIMENTAL))
        self.assertTrue(self.truck.isFull())
        self.truck.conveyBox(uuid)

    def test_convey_box(self):
        self.truck.addFret(self.box1)
        self.truck.conveyBox(self.box1.getIdBox())
        self.assertEqual(self.truck.getCurrentWeight(), 0)

    def test_convey_box_not_found_when_it_have_not_box(self):
        with self.assertRaises(BoxIDError):
            self.truck.conveyBox(uuid4())

    def test_add_fret(self):
        self.truck.addFret(self.box1)
        self.truck.addFret(self.box2)
        self.assertEqual(self.truck.getCurrentWeight(), 9000)
        self.truck.conveyBox(self.box1.getIdBox())
        self.truck.conveyBox(self.box2.getIdBox())

    def test_add_fret_when_its_already_set(self):
        self.truck.addFret(self.box1)
        self.truck.addFret(self.box1)
        self.assertEqual(self.truck.getCurrentWeight(), 1000)

if __name__ == '__main__':
    unittest.main()