import csv
from os import path, remove
from src.utils.error import CsvError

class CsvManager:
    def __init__(self):
        pass #no attributs
    
    """Method that create a csv file"""
    def create_csv(self, rep, data):
        full_rep = path.join(rep)
        try:
            with open(f"{full_rep}", mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except OSError:
            raise CsvError(f"Error while creating csv file in repository : {full_rep}")
    
    """Method that read file data from a specific line and returns it"""
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
    
    """Method for editing a specific line in a csv file"""
    def edit_file(self, rep, line_number, new_line):
        full_rep = path.join(rep)
        data = []
        try:
            with open(full_rep, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                data = list(reader)
            if line_number < 0 or line_number >= len(data):
                raise CsvError(f"Line number {line_number} does not exist in the file.")
            data[line_number] = new_line
            with open(full_rep, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except OSError:
            raise CsvError(f"Error while attempting to edit csv file at repository: {full_rep}")

    """Method that delete a file"""
    def delete_file(self, rep):
        full_rep = path.join(rep)
        try:
            remove(full_rep) #come from os library
        except OSError as e:
            raise CsvError(f"Error while attempting to delete file from repository : {full_rep}")