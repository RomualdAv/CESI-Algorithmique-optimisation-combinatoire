import datetime
import sys
sys.path.insert(0, '../src')
import unittest
from utils.Depot import Depot
from utils.DeliveryWindow import DeliveryWindow


class TestDepot(unittest.TestCase):

    def test_should_instance_depot_when_all_param_is_good(self):
        dw = DeliveryWindow(datetime.time, datetime.time)
        try:
            Depot(1, "depot1", True, dw)
            self.assertEqual(True, True)
        except Exception:
            self.assertEqual(False, True)

    def test_should_instance_depot_when_one_param_isnt_good(self):
        dw = DeliveryWindow(datetime.time, datetime.time)
        with self.assertRaises(ValueError):
            Depot(1, 456, True, dw)

if __name__ == '__main__':
    unittest.main()