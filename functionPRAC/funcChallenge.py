# Author : Joon Son
# Date : 23/Oct/2017
# Description : Practice Function


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        print("can not divide")
        return 0
    else:
        return num1 / num2
number1 = 0
number2 = 0


number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number : "))

print(add(number1, number2))
print(sub(number1, number2))
print(mul(number1, number2))
print(div(number1, number2))



