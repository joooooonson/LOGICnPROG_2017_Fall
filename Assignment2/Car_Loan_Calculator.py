# Author : Joon Son
# Date : 2/Oct/2017
# Description : Car Loan Calculator
# Get the amount of loan, the interest rate (%) and the number of years from user
# display monthly payment
# monthly payment formula
# - monthly payment = (i/1-((1+i)**(-12*n)))*A
# i = r/1200
# r = interest rate(%)
# A = borrowed money at r% interest to purchase a car

# Pseudocode

# 1. get the amount of loan from user and assign to vAmountLoan
# 2. get the interest rate(%) from user and assign to vInterestRate
# 3. get the number of years from user and assign to vYears
# 4. assign result of vInterestRate/1200 to i
# 5. assign result of (i/1-((1+i)**(-12*vYears)))*vAmountLoan to vMonthlyPay
# 6. round vMonthlyPay until after decimal point second
# 7. display the monthly payment

vAmountLoan = float(input("Enter the amount of loan: "))  # set the amount of loan user input to vAmountLoan
vInterestRate = float(input("Enter the interest rate (%): "))  # set the interest rate user input to vInterestRate
vYears = int(input("Enter the number of years: "))  # set the number of years user input to vYears

# evaluate the amount of monthly payment
i = vInterestRate / 1200
vMonthlyPay = vAmountLoan * (i/(1-((1+i)**(-12*vYears))))

# print out result using proper currency formatting
print("Your monthly payment will be ${:.2f}".format(vMonthlyPay))