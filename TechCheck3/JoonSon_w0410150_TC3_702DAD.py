# Author : Joon Son
# Date : 29/Sep/2017
# Description : Tax Withheld Calculator



print("Tax Withholding Calculator")
print("")

ProvincialTaxRate = 0.06
FederalTaxRate = 0.25
TaxDeductionForDependentsRate = 0.02

# UI get information from user
vPreTaxWeeklySalary = float(input("Please enter the full amount of your weekly salary : "))
vNumberOfDependents = int(input("How many dependents do you have ? :"))

# evaluate Tax things
vProvincialTaxWithheld = vPreTaxWeeklySalary * ProvincialTaxRate
vFederalTaxWithheld = vPreTaxWeeklySalary * FederalTaxRate
vDependentTaxDeduction = vPreTaxWeeklySalary * TaxDeductionForDependentsRate * vNumberOfDependents

vTotalWithheld = vProvincialTaxWithheld + vFederalTaxWithheld - vDependentTaxDeduction
vTotalTakeHomePay = vPreTaxWeeklySalary - vTotalWithheld

# output result
print("Provincial Tax Withheld: ${:.2f}".format(round(vProvincialTaxWithheld, 2)))
print("Federal Tax Withheld: ${:.2f}".format(round(vFederalTaxWithheld, 2)))
print("Dependent Deduction for "+str(vNumberOfDependents) + " dependents: ${:.2f}".format(round(vDependentTaxDeduction, 2)))
print("Total Withheld: ${:.2f}".format(round(vTotalWithheld, 2)))
print("Total Take-Home Pay: ${:.2f}".format(round(vTotalTakeHomePay, 2)))

