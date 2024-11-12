import unittest
from src.utils.Types import *

class TestTypes(unittest.TestCase):

    def test_typeOfTruckToUse(self):
        self.assertIn(TypeTruck.OPEN, typeOfTruckToUse(TypeBox.NOTSPECIFY))
        self.assertIn(TypeTruck.REFRIGERATE, typeOfTruckToUse(TypeBox.ALIMENTAL))
        self.assertIn(TypeTruck.WATERTIGHT, typeOfTruckToUse(TypeBox.NOTSPECIFY))
        self.assertIn(TypeTruck.PLATED, typeOfTruckToUse(TypeBox.RADIOACTIVE))

    def test_box_coupling(self):
        self.assertEqual(getBoxCoupling(TypeBox.ALIMENTAL), 7)
        self.assertEqual(getBoxCoupling(TypeBox.FLAMMABLE), 7)
        self.assertEqual(getBoxCoupling(TypeBox.EXPLOSIVE), 7)
        self.assertEqual(getBoxCoupling(TypeBox.TOXIC), 5)

    def test_truck_coupling(self):
        self.assertEqual(getTruckCoupling(TypeTruck.OPEN), 5)
        self.assertEqual(getTruckCoupling(TypeTruck.REFRIGERATE), 7)
        self.assertEqual(getTruckCoupling(TypeTruck.WATERTIGHT), 2)
        self.assertEqual(getTruckCoupling(TypeTruck.PLATED), 0)

    def test_str_to_type_box(self):

        self.assertEqual(str(TypeBox.ALIMENTAL), "ALIMENTAL")
        self.assertEqual(str(TypeBox.FLAMMABLE), "FLAMMABLE")

    def test_str_to_type_truck(self):

        self.assertEqual(str(TypeTruck.OPEN), "OPEN")
        self.assertEqual(str(TypeTruck.PLATED), "PLATED")

if __name__ == '__main__':
    unittest.main()