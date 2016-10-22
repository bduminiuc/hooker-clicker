# coding: utf-8
from csv import DictReader, DictWriter

"""
Class provides methods used for writting and
getting values of csv file as a dict.
"""
class CSVdict:

    def __init__(self, name):
        self.name = name

    def write(self, fieldnames, actions):
        try:
            with open(self.name, "w") as csvfile:
                writer = DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for action in actions:
                    writer.writerow(action)

        except Error:
            print("error")

    def get(self):
        string = ""
        try:
            with open(self.name, newline='') as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    string = string + str(row) + "\n"

        except FileNotFoundError:
            print("No such file:", self.name)

        return string[:-1]


if __name__ == "__main__":
    print("Here is CSVdict class for get csv-dict by name or write it")
