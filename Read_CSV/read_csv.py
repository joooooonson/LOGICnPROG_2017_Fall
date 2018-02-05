# practice for reading csv file
import csv

with open("csv1.txt", "r") as CSV_File:
    dataFromFile = csv.reader(CSV_File)
    for data in dataFromFile:
        print(data)
