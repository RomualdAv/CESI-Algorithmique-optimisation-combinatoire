import unittest
from src.utils.TypeTruck import *
from src.utils.TypeBox import *

class TestTypeTruck(unittest.TestCase):

    def test_should_get_open(self):
        listnotok = [TypeBox.FRAGILE,TypeBox.ALIMENTAL]
        listok = [TypeBox.FLAMMABLE, TypeBox.PRESSURIZED]

        self.assertEqual(typeOfTruckToUse(listok), TypeTruck.OPEN)
        self.assertNotEqual(typeOfTruckToUse(listnotok), TypeTruck.OPEN)

    def test_should_get_refrigerate(self):
        listnotok = [TypeBox.FLAMMABLE, TypeBox.PRESSURIZED]
        listok = [TypeBox.FRAGILE,TypeBox.ALIMENTAL]

        self.assertEqual(typeOfTruckToUse(listok), TypeTruck.REFRIGERATE)
        self.assertNotEqual(typeOfTruckToUse(listnotok), TypeTruck.REFRIGERATE)

    def test_should_get_watertight(self):
        listnotok = [TypeBox.RADIOACTIVE]
        listok = [TypeBox.TOXIC, TypeBox.CORROSIVE]

        self.assertEqual(typeOfTruckToUse(listok), TypeTruck.WATERTIGHT)
        self.assertNotEqual(typeOfTruckToUse(listnotok), TypeTruck.WATERTIGHT)

    def test_should_get_plated(self):
        listok = [TypeBox.TOXIC, TypeBox.RADIOACTIVE,TypeBox.FRAGILE]

        self.assertEqual(typeOfTruckToUse(listok), TypeTruck.PLATED)

if __name__ == '__main__':
    unittest.main()