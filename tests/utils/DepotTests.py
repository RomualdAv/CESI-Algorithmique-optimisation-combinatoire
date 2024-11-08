import unittest
from src.utils.Depot import Depot


class TestDepot(unittest.TestCase):

    def test_should_instance_depot_when_all_param_is_good(self):
        try:
            Depot(1, "depot1")
            self.assertEqual(True, True)
        except Exception:
            self.assertEqual(False, True)

    def test_should_instance_depot_when_one_param_isnt_good(self):
        with self.assertRaises(AttributeError):
            Depot(1, 666)

if __name__ == '__main__':
    unittest.main()