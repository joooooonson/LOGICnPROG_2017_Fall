# Author : Joon Son
# Date : 20/Oct/2017
# Description : Digit Counter
# get an integer between 0 and 10billion from user
# print the number of digits the input has
# use .isdigit() method to validate the input whether it is numeric value or not.

MAXIMUM = 10**10 # 10billion 10000000000
MINIMUM = 0


vInput = 0  # number user input
vCnt = 0  # the number of digits the input has

# welcome message
print("Welcome to the Digit Counter.")

# ask user enter a number ans store it to variable
vInput = input("Enter a number: ")

# if the input user entered is numeric value and it falls within the acceptable numeric range(0 to 10billion)
if vInput.isdigit() and (MINIMUM <= int(vInput) <= MAXIMUM):
    # convert vInput from string to integer and store in variable
    vInputNum = int(vInput)

    # if the input is equal to 10 billions
    if vInputNum == 10**10:
        vCnt = 11
    # if the input is bigger than or equal to billion
    elif vInputNum >= 10**9:
        vCnt = 10
    # if the input is bigger than or equal to 100 millions
    elif vInputNum >= 10**8:
        vCnt = 9
    # if the input is bigger than or equal to 10 millions
    elif vInputNum >= 10**7:
        vCnt = 8
    # if the input is bigger than or equal to million
    elif vInputNum >= 10**6:
        vCnt = 7
    # if the input is bigger than or equal to 100 thousands
    elif vInputNum >= 10**5:
        vCnt = 6
    # if the input is bigger than or equal to 10 thousands
    elif vInputNum >= 10**4:
        vCnt = 5
    # if the input is bigger than or equal to thousand
    elif vInputNum >= 10**3:
        vCnt = 4
    # if the input is bigger than or equal to hundred
    elif vInputNum >= 10**2:
        vCnt = 3
    # if the input is bigger than or equal to ten
    elif vInputNum >= 10:
        vCnt = 2
    # when the input is lower than ten
    else:
        vCnt = 1

    # print result
    print("Digit count result: {}".format(vCnt))

# else it is invalid entry
# print invalid message
else:
    print("Digit count result: Invalid entry")