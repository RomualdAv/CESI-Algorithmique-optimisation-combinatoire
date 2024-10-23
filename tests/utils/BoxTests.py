import datetime
import uuid
import unittest
from src.utils.Box import Box
from src.utils.Size import Size
from src.utils.Depot import Depot
from src.utils.TypeBox import TypeBox
from src.utils.DeliveryWindow import DeliveryWindow


class TestBox(unittest.TestCase):

    def test_should_instance_depot_when_all_param_is_good(self):
        size = Size(2, 3, 4)
        dw = DeliveryWindow(datetime.datetime(2024,10,23,10,0), datetime.datetime(2024,10,23,12,0))
        depot = Depot(1, "depot1", True, dw)
        try:
            Box(uuid.uuid4(), depot, size, TypeBox.RADIOACTIVE)
            self.assertEqual(True, True)
        except Exception:
            self.assertEqual(False, True)

    def test_should_instance_depot_when_one_param_isnt_good(self):
        size = 546
        dw = DeliveryWindow(datetime.datetime(2024,10,23,10,0), datetime.datetime(2024,10,23,12,0))
        depot = Depot(1, "depot1", True, dw)
        with self.assertRaises(AttributeError):
            Box(uuid.uuid4(), depot, size, TypeBox.RADIOACTIVE)

if __name__ == '__main__':
    unittest.main()