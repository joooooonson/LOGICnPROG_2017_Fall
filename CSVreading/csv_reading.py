#Author: Joon Son
#Date: 2017-11-29
#Description: CSV reading challenge
import csv

FILE_PATH = "texts/guests.txt"
READ_MODE = "r"

with open(FILE_PATH, READ_MODE) as myCSV:
    data_from_file = csv.reader(myCSV)

    for line in data_from_file:
        print(" ".join(line))