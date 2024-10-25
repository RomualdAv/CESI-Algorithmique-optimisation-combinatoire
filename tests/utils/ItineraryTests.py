import unittest

from src.utils import Itinerary

class TestInstanceGenerator(unittest.TestCase):

    def test_should_represent_a_itinerary(self):
        itinerary = Itinerary(1,2,[3,4],5.0)
        self.assertEqual(itinerary.get_start_location(), 1)
        self.assertEqual(itinerary.get_end_location(), 2)
        self.assertEqual(itinerary.get_waypoints(), [3,4])
        self.assertEqual(itinerary.get_travel_time(), 5.0)

    def test_encapsulation(self):
        itinerary = Itinerary(1,2,[3,4],5.0)

        waypoints = itinerary.get_waypoints()
        waypoints.append(5)

        self.assertNotEqual(itinerary.get_waypoints(), waypoints)
    def test_should_use_bad_type_of_param(self):
        with self.assertRaises(TypeError):
            itinerary = Itinerary(1,2,3,5.0)
if __name__ == '__main__':
    unittest.main()