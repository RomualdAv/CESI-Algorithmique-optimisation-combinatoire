import unittest
import datetime
from src.utils.DeliveryWindow import DeliveryWindow

class TestDeliveryWindow(unittest.TestCase):

    def test_should_not_get_the_same_object_but_the_same_data(self):
        date1 = datetime.datetime(2021, 5, 17, 9, 0)
        date2 = datetime.datetime(2021, 5, 17, 10, 0)
        window = DeliveryWindow(date1, date2)
        #Check if the objects are different
        self.assertNotEqual(window.getStart, date1)
        self.assertNotEqual(window.getEnd, date2)
        #Check if the data is the same
        self.assertEqual(window.getStart().year, date1.year)
        self.assertEqual(window.getStart().month, date1.month)
        self.assertEqual(window.getStart().day, date1.day)
        self.assertEqual(window.getStart().hour, date1.hour)
        self.assertEqual(window.getStart().minute, date1.minute)
        self.assertEqual(window.getEnd().year, date2.year)
        self.assertEqual(window.getEnd().month, date2.month)
        self.assertEqual(window.getEnd().day, date2.day)
        self.assertEqual(window.getEnd().hour, date2.hour)
        self.assertEqual(window.getEnd().minute, date2.minute)

    def test_should_not_create_an_object_when_the_date_arent_a_datetime(self):
        date1 = datetime.datetime(2021, 5, 17, 9, 0)
        date2 = datetime.datetime(2021, 5, 17, 10, 0)
        with self.assertRaises(AttributeError):
            DeliveryWindow(date1,0)
        with self.assertRaises(AttributeError):
            DeliveryWindow(0,date2)
        with self.assertRaises(AttributeError):
            DeliveryWindow("",0.0)

    def test_should_get_string_of_window(self):
        date1 = datetime.datetime(2021, 5, 17, 9, 0)
        date2 = datetime.datetime(2021, 5, 17, 10, 0)
        window = DeliveryWindow(date1,date2)
        self.assertEqual(str(window), "2021-5-17 9:0 | 2021-5-17 10:0")

if __name__ == '__main__':
    unittest.main()
