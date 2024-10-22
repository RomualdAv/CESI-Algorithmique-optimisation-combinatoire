import datetime
import sys
import uuid
sys.path.insert(0, '../src')
import unittest
from utils.Box import Box
from utils.Size import Size
from utils.Depot import Depot
from utils.TypeBox import TypeBox
from utils.DeliveryWindow import DeliveryWindow


class TestSize(unittest.TestCase):

    def test_should_instance_depot_when_all_param_is_good(self):
        size = Size(2, 3, 4)
        dw = DeliveryWindow(datetime.time, datetime.time)
        depot = Depot(1, "depot1", True, dw)
        try:
            Box(uuid.uuid4(), depot, size, TypeBox.RADIOACTIVE)
            self.assertEqual(True, True)
        except Exception:
            self.assertEqual(False, True)

    def test_should_instance_depot_when_one_param_isnt_good(self):
        size = 546
        dw = DeliveryWindow(datetime.time, datetime.time)
        depot = Depot(1, "depot1", True, dw)
        with self.assertRaises(ValueError):
            Box(uuid.uuid4(), depot, size, TypeBox.RADIOACTIVE)

if __name__ == '__main__':
    unittest.main()