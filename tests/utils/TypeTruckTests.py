import unittest
from src.utils.TypeBox import *

class TestTypeTruck(unittest.TestCase):

    def test_should_get_name(self):
        self.assertEqual(str(TypeTruck.OPEN), "OPEN")
        self.assertEqual(str(TypeTruck.REFRIGERATE), "REFRIGERATE")
        self.assertEqual(str(TypeTruck.WATERTIGHT), "WATERTIGHT")
        self.assertEqual(str(TypeTruck.PLATED), "PLATED")

if __name__ == '__main__':
    unittest.main()