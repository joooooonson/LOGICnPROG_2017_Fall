# Author: Joon Son
# Date: 2017-11-29
# Description: CSV writing challenge
# ask user to input 5 names and ages
# writing those information on the csv file

FILE_PATH = "texts/csvwriting.txt"
WRITING_MODE = "w"
SIZE = 5
lines = []


for i in range(SIZE):
    person = []
    name = input("What is the name of the person No.{}: ".format(i+1))
    age = input("How old is the person No.{}: ".format(i+1))
    person.append(name)
    person.append(age)
    lines.append(person)

myCSV = open(FILE_PATH,WRITING_MODE)

for line in lines:
    myCSV.write(",".join(line)+"\n")

myCSV.close()