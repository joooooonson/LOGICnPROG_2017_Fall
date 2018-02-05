# Author : Joon Son
# Date : 13/Oct/2017
# Description: calculate the cost based on that range’s cost
# Up to and including 1000 cubic feet                               $15.00 flat rate
# Over 1,000 cubic feet and up to and including 2,000 cubic feet    $0.0175 per cubic foot
# Over 2,000 cubic feet and up to and including 3,000 cubic feet    $0.02 per cubic foot
# Over 3,000 cubic feet                                             $70.00 flat rate

# create variables
vAmount = 0.0  # the amount of usage of water user input (cubic feet)
vTotalCharge = 0.0  # Total charge

#  create variables for constant
FIRST_LIMIT = 1000  # First Limit of water usage
SECOND_LIMIT = 2000  # Second Limit of water usage
THIRD_LIMIT = 3000  # Third Limit of water usage

MIN_COST = 15.00  # Minimum cost
MAX_COST = 70  # Maximum cost
RATE_1 = 0.0175  # First rate of charge
RATE_2 = 0.02  # Second rate of charge

# get the amount of usage of water from user
vAmount = float(input("Enter usage of water (cubic feet): "))

# Up to and including 1000 cubic feet : $15.00 flat rate
if vAmount <= 1000:
    vTotalCharge = MIN_COST
# Over 1,000 cubic feet and up to and including 2,000 cubic feet : $0.0175 per cubic foot
elif vAmount > 1000 and vAmount <= 2000:
    vTotalCharge = RATE_1 * vAmount
# Over 2,000 cubic feet and up to and including 3,000 cubic feet : $0.02 per cubic foot
elif vAmount > 2000 and vAmount <= 3000:
    vTotalCharge = RATE_2 * vAmount
# Over 3,000 cubic feet : $70.00 flat rate
else:
    vTotalCharge = MAX_COST

# Display result

print("Total charge is ${:.2f}".format(round(vTotalCharge, 2)))



