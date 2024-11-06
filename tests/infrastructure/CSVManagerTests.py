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
            test_manager = CsvManager("instances", rep,data)
            test_manager.editLine(line, new_data)
            test_manager.delete()
            self.assertEqual(True, True)
        except CsvError:
            self.fail("Test failed, CsvError raised")
        except OSError:
            self.fail("Test failed, OSError raised")

    def test_csv_file_reading_when_it_isnt_created(self):
        rep = "csv-test.csv"
        line = 1

        test_manager = CsvManager("instances", rep)
        with self.assertRaises(CsvError):
            test_manager.readLine(line)

    def test_csv_file_reading_when_it_was_deleted(self):
        rep = "csv-test.csv"
        data = [["column1", "column2", "column3"], ["value1", "value2", "value3"]]
        line = 1

        test_manager = CsvManager("instances", rep,data)
        test_manager.delete()
        with self.assertRaises(CsvError):
            test_manager.readLine(line)
    def test_csv_file_reading_when_line_doesnt_exist(self):
        rep = "csv-test.csv"
        data = [["column1", "column2", "column3"], ["value1", "value2", "value3"]]
        line = 2

        test_manager = CsvManager("instances", rep, data)

        with self.assertRaises(CsvError):
            test_manager.readLine(line)

        test_manager.delete()

    def test_csv_file_reading_when_line_exist(self):
        rep = "csv-test.csv"
        data = [["column1", "column2", "column3"], ["value1", "value2", "value3"]]
        line = 1

        test_manager = CsvManager("instances", rep, data)
        test_manager.readLine(line)
        test_manager.delete()
        self.assertTrue(True)

    def test_csv_file_writing_when_the_data_isnt_string(self):
        rep = "csv-test.csv"
        data = [[12, 12, 12], [12, 12, 12]]
        line = 1

        test_manager = CsvManager("instances", rep, data)
        test_manager.readLine(line)
        test_manager.delete()
        self.assertTrue(True)

    def test_csv_manipulation_when_one_param_isnt_good(self):
        rep = "csv-test.csv"
        data = [["column1", "column2", "column3"], ["value1", "value2", "value3"]]
        line = 6
        new_data = ["value4", "value5", "value6"]

        test_manager = CsvManager("instances", rep, data)

        with self.assertRaises(CsvError):
            test_manager.editLine(line, new_data)

        test_manager.delete()

if __name__ == '__main__':
    unittest.main()