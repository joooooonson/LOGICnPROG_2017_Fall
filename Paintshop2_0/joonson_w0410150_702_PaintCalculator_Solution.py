# Paint Shop Calculator
# Program to calculate the number of gallons of paint required to paint a room, if provided the room dimensions

# Import the math class, for using ceiling rounding
import math

# Declare variable for # of sq. ft. covered by one gallon of paint
square_feet_per_gallon = 150.5

# Intro messages


def welcome_msg():
    print("Welcome to the Paint Shop!")
    print("This program will help you calculate how many cans of paint you need to buy, based on the\
    dimensions of your room.")


def display_result(totalArea, gallons_of_paint):
    # OUTPUT - Display number of gallons needed
    print("\nThe total wall area of your room is {:.2f} square feet.".format(totalArea))
    print("You will need " + str(gallons_of_paint) + " gallon(s) of paint. \n\nHappy Painting!")


def get_totalArea(length, width, height):
    # PROCESSING
    # Calculate the area of the walls
    totalArea = (length * height * 2) + (width * height * 2)
    return totalArea


def get_gallons_of_paint(totalArea):
    # Divide the area by 150 square feet and
    # round number of gallons up to the nearest whole number
    gallons_of_paint = math.ceil(totalArea / square_feet_per_gallon)
    return gallons_of_paint


def run():
    welcome_msg()
    # INPUT
    # Get Dimensions of the room
    length = float(input("\nEnter the length of the room, in feet: "))
    width = float(input("Enter the width of the room, in feet: "))
    height = float(input("Enter the height of the room, in feet: "))

    totalArea = get_totalArea(length, width, height)
    gallons_of_paint = get_gallons_of_paint(totalArea)

    display_result(totalArea, gallons_of_paint)


# start main logic
run()

























