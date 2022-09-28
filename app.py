from ast import main
from operator import delitem

from program_loop import app
import csv

def main():
    # app()
    with open("rooms.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[1])

if __name__ == "__main__":
    main()