# Author : Joon Son
# Date : 21/Oct/2017
# Description : calculate amount of money user made this week
# if the number of hours exceeds 40 in a week, include the amount of overtime pay they made in the total
# overtime pay = 1.5 * usual hourly wage * only number of hours over 40
# ask users to enter the number of hours they worked this week
#   and the dollar amount they make per hour

#
# def getfloat_positive(msg):
#     while(1):
#         try:
#             ifloat = float(input(msg))
#             if ifloat < 0:
#                 print("Please enter a positive number")
#         except ValueError:
#             print("Please enter a floating number")
#             continue
#         break;
#     return ifloat
#

# declaring variables
vWorkedHours = 0.0  # number of hours user worked
vHourlyWage = 0.0  # hourly wage
vTotalWage = 0.0  # total wage

# constant values
OVERTIME_STD = 40  # maximum number of work hour without overtime fee
OVERTIME_RATE = 1.5  # overtime rate

# ask user enter number of hours and hourly wage
vWorkedHours = float(input("Enter number of hours you worked this week :"))
vHourlyWage = float(input("Enter your hourly wage :"))
# vWorkedHours = getfloat_positive("Enter number of hours you worked this week :")
# vHourlyWage = getfloat_positive("Enter your hourly wage :")

# calculate amount of total wage
vTotalWage = vHourlyWage * vWorkedHours

# if the number of hours is over overtime criteria (40 hours)
# add additional wage
if vWorkedHours > OVERTIME_STD:
    vTotalWage += vHourlyWage * (vWorkedHours - OVERTIME_STD) * OVERTIME_RATE

# display result
print("Total wage of this week is ${:.2f}".format(vTotalWage))

