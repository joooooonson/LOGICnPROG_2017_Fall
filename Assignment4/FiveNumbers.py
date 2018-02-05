# Author : Joon Son
# Date : 31/Oct/2017
# Description :
# Prompt the user to enter five numbers, and store them in the program.
# Reverse the five numbers from the user-entered order and display the reversed order onscreen.
# Calculate and display the average of the five numbers
# Display a list of all numbers that are larger than the calculated average.


# list of numbers, to verify validity of input
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# size of list
SIZEOFLIST = 5

# list variable to store user inputs
inputList = []


# def get_int(str):
#     # get user input as a integer
#     # check user input if it is numeric value or not
#     # if it is not numeric ask user enter again
#     while True:
#         input_valid = True
#         input_value = input(str)
#         for temp in input_value:
#             if temp not in NUMBERS:
#                 input_valid = False
#
#         if not input_valid :
#             print("Please Enter Integer Value")
#             continue
#         else:
#             break
#     return int(input_value)

def get_int(str):
    # get user input as a integer
    # check user input if it is numeric value or not
    # if it is not numeric ask user enter again
    while(True):
        try:
            input_value = int(input(str))
        except ValueError :
            print("Please Enter Integer Value")
            continue
        else:
            break
    return input_value

# get user inputs and sum all the inputs
for i in range(SIZEOFLIST):  # SIZE OF LIST = 5
    num = get_int("Enter Value #{} : ".format(i+1))
    # add the number to list of input
    inputList.append(num)
print("-"*50)

# reverse order list
print("Numbers in reverse order")

# change order of items in the list to reverse order
inputList.reverse()

# print all the items of the list
for temp in inputList:
    print(temp)
print("-"*50)

# evaluate average and print the average
avg = sum(inputList) / len(inputList)
print("The average of the numbers is : {:.1f}".format(avg))
print("-"*50)

print("Numbers greater than the average")
# if the item is greater than average, print it
for temp in inputList:
    if temp > avg:
        print(temp)

