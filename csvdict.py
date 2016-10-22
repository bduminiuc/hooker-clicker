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
    filename = "temp.csv"
    fieldnames = ['mouse_x', 'mouse_y', 'action']
    csvfile = CSVdict(filename)
    actions = [
        {'mouse_x': '100', 'mouse_y': '100', 'action':'click'},
        {'mouse_x': '200', 'mouse_y': '200', 'action':'dbclick'},
        {'mouse_x': '300', 'mouse_y': '300', 'action':'click'}
    ]
    
    csvfile.write(fieldnames, actions)
    print(csvfile.get())
