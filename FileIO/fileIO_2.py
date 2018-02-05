# Author : Joon Son
# Date : 14/Nov/2017
# Practice file input output 2
import os
# create file object
# if the file does not exist, error occurs "FileNotFoundError"
try:
    fo = open("readtest_r.txt", "r")
except FileNotFoundError:
    print("Can not find the file")

try:
    fo = open("readtest_rplus.txt", "r+")
except FileNotFoundError:
    print("Can not find the file")

# make directory!!!
# os.mkdir("../FileInputOutput")
# os.mkdir("../FileInputOutput/TestFiles")
# just create file, failing if the file already exist "FileExistsError
try:
    fo = open("../FileInputOutput/TestFiles/testfile.txt", "x")
except FileExistsError:
    print("The file already exists")

try:
    fo.close()
except NameError:
    print("File object is not defined!!")

# if the file does not exist, create new file and overwrite
fo_w = open("../FileInputOutput/TestFiles/testfile.txt", "w")
str_input = "I am so good student\nand I am gonna be a super star!!!\n"
fo_w.write(str_input)
fo_w.close()

# if the file does not exist, error
fo_r = open("../FileInputOutput/TestFiles/testfile.txt", "r")
str_output = fo_r.read(10)
print(str_output)
fo_r.close()

# if the file is not there, FileNotFoundError
try:
    fo_rplus = open("../FileInputOutput/TestFiles/testplus", "r+")
except FileNotFoundError:
    print("No file!!")
else:
    str_output = fo_rplus.read(10)
    print("test 1 :", str_output)
    fo_rplus.close()

fo_wplus = open("../FileInputOutput/TestFiles/testplus", "w+")
fo_wplus.write("Hello~~~\nNice to meet you\nhere is wrtie plus test file!!!")
position = fo_wplus.tell()
print("current file posiont is located at : ", position)
fo_wplus.seek(0,0)
position = fo_wplus.tell()
print("current file posiont is located at : ", position)
str_output = fo_wplus.read(30)
print("test 2 :", str_output)
fo_wplus.close()










