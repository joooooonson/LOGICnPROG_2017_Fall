# Author : Joon Son
# Date : 03/Oct/2017
# Description : convert a distance given in miles, yards, feet and inches to
#              the metric equivalent length in kilometer, meters, and centimetres.
#              make user be able to input the numbers of miles, yards, feet, and inches
#              convert the length from user entirely into inches and then divided by 39.37
#              formula
#              1. total inches = 63360*miles + 36*yards + 12*feet + inches
#              2. total metres = total inches/39.37
#              3. kilometers = int(metres/ 1000)

# PSEUDOCODE
# 1. get the number of miles from user and assign it to vMiles
# 2. get the number of yards from user and assign it to vYards
# 3. get the number of feet from user and assign it to vFeet
# 4. get the number of inches from user and assign it to vInches
# 5. evaluate total inches by using formula 1 and assign it to vTotalInches
# 6. evaluate total meters by using formula 2 and assign it to vTotalMeters
# 7. evaluate the number of kilometers by using formula 3 and assign it to vKiloMeters
# 8. evaluate the number of kilometers ( int(vTotalMeters - vKiloMeters*1000)) and assign it to vMeters
# 9. evaluate the number of centimeters ( (vTotalMeters - int(vTotalMeters))*100  ) and
#    assign it to vCentimeters
# 10. display the distance in kilometer, meters, and centimeters. the number of centimeters should be
#    displayed to one decimal place.

vMiles = float(input("Enter the number of miles: "))  # get the number of miles from user and set to vMiles
vYards = float(input("Enter the number of yards: "))  # get the number of yards from user and set to vYards
vFeet = float(input("Enter the number of feet: "))  # get the number of feet from user and set to vFeet
vInches = float(input("Enter the number of inches: "))  # get the number of inches from user and set to vInches

# evaluate total inches
vTotalInches = 63360 * vMiles + 36 * vYards + 12 * vFeet + vInches

# convert from inch to meter
vTotalMeters = vTotalInches / 39.37

# get the number of kilometers
vKiloMeters = int(vTotalMeters / 1000)

# get the number of meters
vMeters = int(vTotalMeters - vKiloMeters*1000)

# get the number of centimeters
vCentiMeters = (vTotalMeters - int(vTotalMeters)) * 100

# print out result
print("The Metric length is {0} kilometers, {1} metres, and {2:.1f} centimetres.".format(vKiloMeters, vMeters,
                                                                                         round(vCentiMeters, 1)))
