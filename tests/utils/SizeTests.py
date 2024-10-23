import unittest
from src.utils.Size import Size

class TestSize(unittest.TestCase):

    def test_should_get_volume_when_values_is_positive(self):
        size = Size(2, 3, 4)
        self.assertEqual(size.getVolume(), 24)

    def test_should_get_volume_when_values_is_not_positive(self):
        with self.assertRaises(ValueError):
            Size(0, -3, 4)

    def test_should_get_string_of_size(self):
        size = Size(2, 3, 4)
        self.assertEqual(str(size), "(width :2, height :3, length :4)")

if __name__ == '__main__':
    unittest.main()