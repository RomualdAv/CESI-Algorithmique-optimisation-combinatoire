import csv
from os import path, remove
from src.utils.error import CsvError

class CsvManager:
    def __init__(self):
        pass #no attributs

    """Method that creates a csv file
    rep = repository path such as : "instances/filename.csv"
    data = raw data to write in the file, example : [["column1", "column2", "column3"], ["value1", "value2", "value3"]]
    """
    def create_csv(self, rep, data):
        full_rep = path.join(rep)
        try:
            with open(f"{full_rep}", mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except OSError:
            raise CsvError(f"Error while creating csv file in repository : {full_rep}")

    """Method that reads file data from a specific line and returns it
    rep = repository path such as : "instances/filename.csv"
    line = line number you wanna read (0 = header values)
    """
    def read_csv(self, rep, line):
        full_rep = path.join(rep)
        try:
            with open(full_rep, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for current, l in enumerate(reader):
                    if current == line:
                        return l
                raise CsvError(f"Line number {line} does not exist in the file.")
        except OSError:
            raise CsvError(f"Error while attempting to read csv file at repository: {full_rep}")

    """Method for editing a specific line in a csv file
    rep = repository path such as : "instances/filename.csv"
    line = line number you wanna read (0 = header values)
    new_line = content you wanna insert such as : ["value1", "value2", "value3"]
    """
    def edit_file(self, rep, line, new_line):
        full_rep = path.join(rep)
        data = []
        try:
            with open(full_rep, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                data = list(reader)
            if line < 0 or line >= len(data):
                raise CsvError(f"Line number {line} does not exist in the file.")
            data[line] = new_line
            with open(full_rep, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except OSError:
            raise CsvError(f"Error while attempting to edit csv file at repository: {full_rep}")

    """Method that deletes a file
    rep = repository path such as : "instances/filename.csv"
    """
    def delete_file(self, rep):
        full_rep = path.join(rep)
        try:
            remove(full_rep) #come from the os library
        except OSError as e:
            raise CsvError(f"Error while attempting to delete file from repository : {full_rep}")