# Author : Joon Son
# Date : 2/Oct/2017
# Description : PC Repair Shop. 

# Get the customer's name, the number of hours of labour
# , the cost of any required parts or supplies from user
# Display the customer's name, labour cost, parts cost and total cost
# $65 per hour for labour
# costs for parts and supplies are subject to a 15% sales tax.

# Pseudocode
# 1. assign 65 to LABOURCOSTRATE
# 2. assign 0.15 to SALESTAXRATE
# 3. get customer's name from user and assign to vCustName
# 4. get the number of hours of labour from user and assign to vLabourHour
# 5. get the cost of any required parts or supplies from user and assign to vCostParts
# 6. assign result of product vLabourHour and LABOURCOSTRATE to vCostLabour
# 7. assign result of product (1 + SALESTAXRATE) and vCostParts to vTaxedCostParts
# 8. assign result of sum vCostLabour and vTaxedCostParts to vTotalCost
# 9. round all the currency values ( labour cost, parts cost, total cost )
# 10. display the customer's name
# 11. labour cost, parts cost and total cost

# set constant value ( labour cost per hour -> LABOURCOSTRATE, sales tax rate -> SALESTAXRATE ) to variables
LABOURCOSTRATE = 65
SALESTAXRATE = 0.15

# print out welcome message
print("McNair's PC Repair - Word order Tracking Program\n")

vCustName = input("Enter the customer's name: ")  # get the customer's name from user and set to vCustName
# get the number of hours of labour and set to vLabourHour
vLabourHour = float(input("Enter the number of hours of labour: "))
# get the cost of any parts and/or supplies from user and set to vCostParts
vCostParts = float(input("Enter the cost of any parts and/or supplies: "))

# evaluate cost for total labour
vCostLabour = vLabourHour * LABOURCOSTRATE
# evaluate cost for parts or supplies applied by sales tas rate
vTaxedCostParts = vCostParts * (1 + SALESTAXRATE)
# get total cost
vTotalCost = vCostLabour + vTaxedCostParts


# print out result using proper currency formatting
print("Work order summary for customer {}".format(vCustName))
print("Labour cost: ${:.2f}".format(round(vCostLabour, 2)))
print("Parts cost: ${:.2f}".format(round(vTaxedCostParts, 2)))
print("Total cost: ${:.2f}".format(round(vTotalCost, 2)))
