from csv import writer, reader
from os import path, remove
from typing import Any

from src.infrastructure.error import CsvError

class CsvManager:
    def __init__(self,directory: str, filename: str, data: list[list[Any]] = None):
        """
        Constructor of the class
        :param directory: directory to the file
        :param filename: name of the file with an extension
        :param data: data to insert in the file such as : [["column1", "column2", "column3"], ["value1", "value2", "value3"]] if the file does not exist else don't put anything

        :raises CsvError: if the file cannot be created
        """

        self.directory = path.join(directory,filename)
        self.filename = filename
        if data is not None:
            self.__create__(data)

    def __create__(self,data: list[list[Any]]):
        """
        Method that creates a csv file

        :param data: data to insert in the file such as : [["column1", "column2", "column3"], ["value1", "value2", "value3"]]

        :raises CsvError: if the file cannot be created
        """
        try:
            with open(f"{self.directory}", mode='w', newline='', encoding='utf-8') as f:
                writer(f).writerows(data)
        except OSError:
            raise CsvError(f"Error while creating csv file in repository : {self.directory}")

    def readLine(self, line):
        """
        Method that reads file data from a specific line and returns it

        :param line: line number you want to read (0 = header values)

        :raises CsvError: if the line number does not exist in the file
        :raises CsvError: if the file cannot be read
        """
        try:
            with open(self.directory, mode='r', newline='', encoding='utf-8') as f:
                reader_data = reader(f)
                for current, l in enumerate(reader_data):
                    if current == line:
                        return l
                raise CsvError(f"Line number {line} does not exist in the file: {self.filename}.")
        except OSError:
            raise CsvError(f"Error while attempting to read csv file: {self.filename}")

    def editLine(self, line, new_line):
        """
        Method for editing a specific line in a csv file

        :param line: line number you want to read (0 = header values)
        :param new_line: content you want to insert such as : ["value1", "value2", "value3"]

        :raises CsvError: if the line number does not exist in the file
        :raises CsvError: if the file cannot be edited
        """
        try:
            with open(self.directory, mode='r', newline='', encoding='utf-8') as f:
                reader_data = reader(f)
                data = list(reader_data)
            if line < 0 or line >= len(data):
                raise CsvError(f"Line number {line} does not exist in the file: {self.filename}.")
            data[line] = new_line
            with open(self.directory, mode='w', newline='', encoding='utf-8') as f:
                writer_data = writer(f)
                writer_data.writerows(data)
        except OSError:
            raise CsvError(f"Error while attempting to edit csv file: {self.filename}")

    def addLine(self,line):
        """
        Method that adds a line to the end of the file

        :param line: content you want to insert such as : ["value1", "value2", "value3"]

        :raises CsvError: if the file cannot be modified
        """
        try:
            with open(self.directory, mode='r', newline='', encoding='utf-8') as f:
                reader_data = reader(f)
                data = list(reader_data)
            data.append(line)
            with open(self.directory, mode='w', newline='', encoding='utf-8') as f:
                writer_data = writer(f)
                writer_data.writerows(data)
        except OSError:
            raise CsvError(f"Error while attempting to modified csv file: {self.filename}")

    def delete(self):
        """
        Method that deletes a file

        :raises CsvError: if the file cannot be deleted
        """
        try:
            remove(self.directory)
        except OSError:
            raise CsvError(f"Error while attempting to delete file from repository : {self.directory}")