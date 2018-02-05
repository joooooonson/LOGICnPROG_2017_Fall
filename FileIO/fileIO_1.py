# Author: Joon Son
# Date: 14/Nov/2017
# Description: Practice Python File Input Output 1

# default File I/O
# stdin and stdout

# print function uses stdout file (default: monitor)
# print("print function output strings on stdout file which is monitor")

# input function uses stdin file (default: keyboard)
# raw_input - python 2.x
# input = python 3.x
# difference between raw_input and input is that input function assumes the input is a valid python expression
# and returns the evaluated result

# str1 = eval(input("Enter your result : ")) # [x*5 for x in range(2, 10, 2)] -> [10, 20, 30, 40]
# print("Received input is : ", str1)

# Opening and Closing Files
# file object = file
# exactly file object is set of methods and attributes to manipulate the file

# create file object
# syntax
# file object = open(file_name, [, access_mode][, buffering])

# parameter details -
#       file_name = file name
#       access_mode = r - read only, w - write only , a - append only ....
#       buffering = 0 - no buffering, 1- line buffering, .... negative - default behavior

# access modes detail
# ===============================================================================================
# text file
# ===============================================================================================
# access mode   | description
# r             | reading only. file pointer is placed at the beginning of the file. default mode
# r+            | reading and writing. file pointer is placed at the beginning of the file.
# w             | writing only. Overwrites the file if the file exists. If the file does not exist
#               | , creates a nes file.
# w+            | writing and reading. Overwrites the file if the file exists. If the file does
#               | not exist, creates a nes file.
# a             | appending. file pointer is placed at the end of the file if the file exists. If
#               | the file does not exist, creates a nes file.
# a+            | appending and reading. file pointer is placed at the end of the file if the file
#               | exists. If the file does not exist, creates a nes file.
# ================================================================================================
# binary file
# ================================================================================================
# access mode   | description
# rb            | reading only in binary format. file pointer is placed at the beginning of the
#               | file. default mode
# rb+           | reading and writing in binary format. file pointer is placed at the beginning of
#               | the file.
# wb            | writing only in binary format. Overwrites the file if the file exists. If the
#               | file does not exist, creates a nes file.
# wb+           | writing and reading in binary format. Overwrites the file if the file exists. If
#               | the file does not exist, creates a nes file.
# ab            | appending in binary format. file pointer is placed at the end of the file if the
#               | file exists. If the file does not exist, creates a nes file.
# ab+           | appending and reading in binary format. file pointer is placed at the end of the file if the file
#               | exists. If the file does not exist, creates a nes file.


# File object Attributes
# file.closed   | Return true, if file is closed, false otherwise.
# file.mode     | Return access mode with which file was opened.
# file.name     | Return name of the file.
# file.softspace| Return false if space explicitly required with print, true otherwise. ????

myFileObject = open("myfile.txt", "w+")

print("Name of the file: ", myFileObject.name)
print("Mode of the file: ", myFileObject.mode)
print("Cloased or not: ", myFileObject.closed)
# print("softspace : ", myFileObject.softspace)

position = myFileObject.tell()
print("current position is placed at :", position)

# the write() method
myFileObject.write("Joon is a good student.\nand he is gonna be a super star!!\n")
position = myFileObject.tell()
print("current position is placed at :", position)
str2 = myFileObject.read(10)
print(str2)

# return current position
position = myFileObject.tell()
print("current position is placed at :", position)

# reposition pointer
# syntax
# fileobject.seek(offset[,from])
# offset = number of bytes to be moved
# from = reference position
#      = 0 - beginning of the file
#      = 1 - current position
#      = 2 - end of the file
myFileObject.seek(0, 0)
str2 = myFileObject.read(10)
print(str2)
position = myFileObject.tell()
print("current position is placed at :", position)

myFileObject.close()

