# Author : Joon Son
# Date : 13/Oct/2017
# Description : computes taxes

# If your status is ‘Single’ and
# if the taxable income is over	but not over	the tax is	of the amount over
# $0	                            $8,000	    10%	                    $0
# $8,000	                        $32,000	    $800 + 15%	            $8,000
# $32,000		                                $4,400 + 25%	        $32,000
# If your status is ‘Married’ and
# if the taxable income is over	but not over	the tax is	of the amount over
# $0	                            $16,000	    10%	                    $0
# $16,000	                        $64,000	    $1,600 + 15%	        $16,000
# $64,000		                                $8,800 + 25%	        $64,000

# Create variables
vStatus = ""        # customer's status single or married
vIncome = 0.0       # customer's taxable income
vTotalTax = 0.0     # total tax
vFirstLimit = 0     # First limit of income in tax schedule (8000 or 16000)
vSecondLimit = 0    # Second limit of income in tax schedule (32000 or 64000)

# Create variables for constant
STATUS1 = "SINGLE"  # single status
STATUS2 = "MARRIED" # marital status
RATE_1 = 0.1        # tax rate (when income is not over first limit)
RATE_2 = 0.15       # tax rate (when income is over first limit but not over second limit)
RATE_3 = 0.25       # tax rate (when income is over second limit)
SINGLE_LIMIT_1 = 8000   # first limit for single status
SINGLE_LIMIT_2 = 32000   # second limit for single status
MARITAL_LIMIT_1 = 16000   # first limit for marital status
MARITAL_LIMIT_2 = 64000   # second limit for marital status

# Get marital status and the amount of income from user
vStatus = input("Enter your marital status (Single / Married): ")
vIncome = float(input("Enter your taxable income: "))

# make the value of vStatus in upper case
vStatus = vStatus.upper()

# when the customer is single, first limit would be 8000 and second limit would be 32000
if vStatus == STATUS1:
    vFirstLimit = SINGLE_LIMIT_1
    vSecondLimit = SINGLE_LIMIT_2
# when the customer is marital, first limit would be 16000 and second limit would be 64000
elif vStatus == STATUS2:
    vFirstLimit = MARITAL_LIMIT_1
    vSecondLimit = MARITAL_LIMIT_2

# when the amount of income is not over first limit
if vIncome <= vFirstLimit:
    vTotalTax += vIncome * RATE_1
# when the amount of income is over first limit but not over second limit
elif vIncome > vFirstLimit and vIncome <= vSecondLimit:
    vTotalTax += ( vFirstLimit * RATE_1 ) + (vIncome - vFirstLimit) * RATE_2
# when the amount of income is over second limit
else:
    vTotalTax += ( vFirstLimit * RATE_1 + (vSecondLimit - vFirstLimit) * RATE_2 ) + (vIncome - vSecondLimit) * RATE_3

# Display result
print("Your total tax is ${:.2f}".format(round(vTotalTax, 2)))




