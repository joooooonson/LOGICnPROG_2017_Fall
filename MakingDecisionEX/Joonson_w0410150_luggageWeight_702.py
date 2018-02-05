# Author : Joon Son
# Date : 21/Oct/2017
# Description : calculate whether a surcharge is required or not depending on weight of luggage
# maximum luggage weight = 50lbs
# surcharge fee = $25
# ask user to enter the total weight of their luggage


# def getfloat_positive(msg):
#     while True:
#         try:
#             vNum = float(input(msg))
#             if vNum < 0:
#                 print("Please enter a positive number")
#         except ValueError:
#             print("Please enter a floating number")
#             continue
#         break
#     return vNum

# declaring variable
vTotalWeight = 0  # total weight of luggage

# constant values
MAX_WEIGHT = 50  # Maximum weight without surcharge
SURCHARGE = 25  # amount of surcharge

# vTotalWeight = getfloat_positive("Enter total weight of luggage: ")
vTotalWeight = float(input("Enter total weight of luggage: "))

# when total weight is over maximum weight display amount of surcharge
if vTotalWeight > MAX_WEIGHT :
    print("Surcharge is required ({})".format(SURCHARGE))
# else no surcharge
else:
    print("Surcharge is NOT required")
