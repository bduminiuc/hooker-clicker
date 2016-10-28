# coding: utf-8
from csv import DictReader, DictWriter

"""
Class provides methods used for writing and
getting values of csv file as a dict.
"""


class CsvDict:

    def __init__(self, name):
        self.name = name

    def write(self, fieldnames, actions):
        try:
            with open(self.name, "w") as csv_file:
                writer = DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                for action in actions:
                    writer.writerow(action)

        except Exception as e:
            print(e.args)

    def get(self):
        actions = []
        try:
            with open(self.name, newline='') as csv_file:
                reader = DictReader(csv_file)
                for row in reader:
                    actions.append(row)

        except FileNotFoundError:
            print("No such file:", self.name)

        return actions


if __name__ == "__main__":
    pass
