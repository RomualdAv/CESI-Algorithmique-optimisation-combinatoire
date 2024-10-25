import unittest
from src.utils.TypeBox import TypeBox
from src.utils.error import TruckError
from src.utils.TypeTruck import TypeTruck

class TestTypeBox(unittest.TestCase):

    def test_isPossibleToTransport(self):
        # Test case where transportation is possible
        self.assertTrue(TypeBox.ALIMENTAL.isPossibleToTransport([TypeBox.NOTSPECIFY]))

        # Test case where transportation is not possible
        self.assertFalse(TypeBox.ALIMENTAL.isPossibleToTransport([TypeBox.FLAMMABLE]))

    def test_typeOfTruckToUse(self):
        # Test cases for typeOfTruckToUse method
        self.assertIn(TypeTruck.OPEN, TypeBox.NOTSPECIFY.typeOfTruckToUse())
        self.assertIn(TypeTruck.REFRIGERATE, TypeBox.NOTSPECIFY.typeOfTruckToUse())
        self.assertIn(TypeTruck.WATERTIGHT, TypeBox.NOTSPECIFY.typeOfTruckToUse())
        self.assertIn(TypeTruck.PLATED, TypeBox.NOTSPECIFY.typeOfTruckToUse())

    def test_str(self):
        # Test the string representation of the enum
        self.assertEqual(str(TypeBox.ALIMENTAL), "ALIMENTAL")
        self.assertEqual(str(TypeBox.FLAMMABLE), "FLAMMABLE")

if __name__ == '__main__':
    unittest.main()