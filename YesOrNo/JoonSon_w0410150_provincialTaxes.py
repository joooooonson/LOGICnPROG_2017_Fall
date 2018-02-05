# Author : Joon Son
# Date : 16/Oct/2017
# Description : Calculate the total to charge for an order from an online store
# get name of country and order total from user
# if the country is Canada, ask which province
# if the country is not Canada do not charge any taxes.
# if the country is Canada calculate tax based on the province
#               Alberta 5%
#               Ontario, New Brunswick, Nova Scotia 15%
#               Other 6% + 5%
# print total tax for their order

COUNTRY = "CANADA"

TAX_1 = 0.05  # TAX RATE for ALBERTA
TAX_2 = 0.15  # Tax rate for ontario, new brunswick, nova scotia
TAX_3 = 0.11  # Tax rate for other province

vCountry = ""  # variable for name of country
vProvince = ""  # variable for name of province
vTotalOrder = 0.0  # variable for amount of total order
vTotalTax = 0.0  # variable for amount of total tax

# get name of country and order total from user
vCountry = input("Where do you order? (name of country):").upper()
vTotalOrder = float(input("Enter a amount of total order : "))

# when the country is CANADA, ask which province
if vCountry == COUNTRY:
    vProvince = input("Which province? :").upper()
    # if alberta, tax rate is 5%
    if vProvince == "ALBERTA":
        vTotalTax = vTotalOrder * TAX_1
    # if ontario, new brunswick, nova scotia , tax rate is 15%
    elif vProvince == "ONTARIO" or vProvince == "NEW BRUNSWICK" or vProvince == "NOVA SCOTIA":
        vTotalTax = vTotalOrder * TAX_2
    # if other provinces, tax rate is 11%
    else:
        vTotalTax = vTotalOrder * TAX_3
# else the country is outside of canada, No tax is charged
else:
    vTotalTax = 0.0

# print total order with total tax
print("Total Tax : ${:.2f}".format(vTotalTax + vTotalOrder))


