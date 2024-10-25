import unittest
from src.infrastructure.CSVManager import CsvManager
from src.utils.error import CsvError


class TestCsvManager(unittest.TestCase):

    def test_csv_manipulation_when_all_param_is_good(self):
        rep = "csv-test.csv"
        data = [["column1", "column2", "column3"], ["value1", "value2", "value3"]]
        line = 1
        new_data = ["value4", "value5", "value6"]

        try:
            testManager = CsvManager()
            testManager.create_csv(rep, data)
            testManager.edit_file(rep, line, new_data)
            testManager.delete_file(rep)
            self.assertEqual(True, True)
        except Exception:
            self.assertEqual(False, True)

    def test_csv_manipulation_when_one_param_isnt_good(self):
        rep = "csv-test.csv"
        data = [["column1", "column2", "column3"], ["value1", "value2", "value3"]]
        line = 6
        new_data = ["value4", "value5", "value6"]

        with self.assertRaises(CsvError):
            testManager = CsvManager()
            testManager.create_csv(rep, data)
            testManager.edit_file(rep, line, new_data)
            testManager.delete_file(rep)

if __name__ == '__main__':
    unittest.main()


"""
Code pour test

import unittest
from tests.infrastructure.CSVManagerTests import TestCsvManager

if __name__ == '__main__':
    suite = unittest.TestSuite()

    # Ajouter chaque test manuellement
    suite.addTest(TestCsvManager('test_csv_manipulation_when_all_param_is_good'))
    suite.addTest(TestCsvManager('test_csv_manipulation_when_one_param_isnt_good'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
"""