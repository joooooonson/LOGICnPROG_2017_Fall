# Author : Joon son
# Date : 13/Oct/2017
# Description : The price computed as follows:
# The charge for all desks is a minimum $200.
# If the surface (length * width) is over 750 square inches, add $50.
# For every drawer in the desk, there is an additional $30 charge.

# create variables
vOrderNumber = ""  # order number
vLength = 0.0  # length of desk
vWidth = 0.0  # width of desk
vWoodType = ""  # the type of wood (mahogany, oak, pine)
vNumOfDrawers = 0  # the number of drawers
vTotalCost = 0.0  # total cost for order
vSurface = 0.0  # surface of desk

# create variables for Constant
MIN_COST = 200  # minimum cost of desk
REG_SURFACE = 750  # regular surface of desk.
COST_FOR_SUR = 50  # additional fee for big surface
TYPE1 = 'mahogany'  # mahogany type has additional fee
TYPE2 = 'oak'  # oak type has additional fee
TYPE1_COST = 150  # additional fee for mahogany type
TYPE2_COST = 125  # additional fee for oak type
COST_DRAWER = 30  # additional fee for each drawers

# get information from user and assign it to variables
vOrderNumber = input("Enter order number: ")
vLength = float(input("Enter length of desk (inches): "))
vWidth = float(input("Enter width of desk (inches): "))
vWoodType = input("Enter the type of wood (mahogany, oak, pine): ")
vNumOfDrawers = int(input("Enter number of drawers: "))

#  evaluate surface of desk
vSurface = vLength * vWidth

# make value of vWoodType to lowercase
vWoodType = vWoodType.lower()

# calculate total cost
vTotalCost = MIN_COST

# if the surface is over regular surface add additional fee
if vSurface > REG_SURFACE:
    vTotalCost += COST_FOR_SUR

# if the wood is "mahogany", add 150; for "oak" add 125
# no charge for "pine"

if vWoodType == TYPE1:
    vTotalCost += TYPE1_COST
elif vWoodType == TYPE2:
    vTotalCost += TYPE2_COST

# For every drawer in the desk, there is an additional 30 charge

vTotalCost += vNumOfDrawers * COST_DRAWER

# Display result

print("The total cost for order {} is: {:.2f}".format(vOrderNumber, round(vTotalCost, 2)))




