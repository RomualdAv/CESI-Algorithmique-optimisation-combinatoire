import unittest
from src.infrastructure.CSVManager import *


class TestCSVManager(unittest.TestCase):

    def test_should_instance_depot_when_all_param_is_good(self):
        dw = DeliveryWindow(datetime.datetime(2024,1,1,13,30), datetime.datetime(2024,1,1,15,30))
        try:
            Depot(1, "depot1", True, dw)
            self.assertEqual(True, True)
        except Exception:
            self.assertEqual(False, True)

    def test_should_instance_depot_when_one_param_isnt_good(self):
        dw = DeliveryWindow(datetime.datetime(2024,1,1,13,30), datetime.datetime(2024,1,1,15,30))
        with self.assertRaises(AttributeError):
            Depot(1, 666, True, dw)

if __name__ == '__main__':
    unittest.main()