import uuid
import unittest
from src.utils.Box import Box
from src.utils.Size import Size
from src.utils.Depot import Depot
from src.utils.Types import TypeBox

class TestBox(unittest.TestCase):

    def test_should_instance_depot_when_all_param_is_good(self):
        size = Size(2, 3, 4)
        depot = Depot(1, "depot1")
        try:
            Box(uuid.uuid4(), depot, size, TypeBox.RADIOACTIVE)
            self.assertEqual(True, True)
        except Exception:
            self.assertEqual(False, True)

    def test_should_instance_depot_when_one_param_isnt_good(self):
        size = 546
        depot = Depot(1, "depot1")
        with self.assertRaises(AttributeError):
            Box(uuid.uuid4(), depot, size, TypeBox.RADIOACTIVE)

if __name__ == '__main__':
    unittest.main()