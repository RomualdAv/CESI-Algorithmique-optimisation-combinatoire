import unittest
from src.utils.TypeBox import TypeBox
from src.utils.error import UncreatedTypeError


class TestTypeBox(unittest.TestCase):

    def test_isPossibleToTransport(self):
        # Test case where transportation is possible
        self.assertTrue(TypeBox.ALIMENTAL.isPossibleToTransport([TypeBox.NOTSPECIFY]))

        # Test case where transportation is not possible
        self.assertFalse(TypeBox.ALIMENTAL.isPossibleToTransport([TypeBox.FLAMMABLE]))

    def test_str(self):
        # Test the string representation of the enum
        self.assertEqual(str(TypeBox.ALIMENTAL), "ALIMENTAL")
        self.assertEqual(str(TypeBox.FLAMMABLE), "FLAMMABLE")


if __name__ == '__main__':
    unittest.main()