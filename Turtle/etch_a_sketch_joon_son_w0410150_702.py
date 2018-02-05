 # Create a Turtle Etch-A-Sketch program!
# Allow the user to draw one line at a time
# User can enter the:
#   Color of the current line (ie. Red, blue, green)
#   Length of the current line (distance in pixels)
#   Direction of the current line (Left, Right, Straight, Back, None)
#   The user should be able to draw any number of lines
#   The program will continue until the user types exit at a prompt
#   Use try blocks to validate user-entered data.
# User should only be able to enter:
#   Valid color values
#   Valid directions (Left, Right, Straight, Back or None)
#   A numeric value for distance in pixel

import turtle
colors = ["red", "yellow", "blue", "green", "pink", "purple", "orange", "black", "cyan", "magenta"]
directions = ["left", "right", "straight", "back", "none"]
prev_direction = ""
user_input = ""

kkobo = turtle.Turtle()
kkobo.speed(1)
kkobo.shape("turtle")
kkobo.pensize(1)


def print_instructions():
    print("* Turtle" + "*" * 30)
    print("* You can draw one line at a time")
    print("* Enter the color of the current line (ie. Red, Blue, Green)")
    print("* Enter the length of the current line (distance in pixels)")
    print("* Enter the Direction of the current line (Left, Right, Straight, Back, None")
    print("* Type exit to quit")

print_instructions()

user_input = input("Please enter to start.....(exit to quit) >")
while user_input.lower() != 'exit':
    in_color = ""
    in_direction = ""
    in_distance = 0
    while in_color not in colors:
        user_input = input("> color: ").lower()
        if user_input in colors:
            in_color = user_input
        else:
            print("*" * 50)
            print("valid color lists")
            print("red, yellow, blue, green, pink, purple, orange, black, cyan, magenta")

    while True:
        try:
            user_input = int(input("> distance: "))
        except ValueError:
            print("*"*50)
            print("Please enter integer value")
            continue
        else:
            in_distance = user_input
            break

    while in_direction not in directions:
        user_input = input("> direction: ").lower()
        if user_input in directions:
            in_direction = user_input
            prev_direction = in_direction
        elif user_input == "" and prev_direction != "":
            in_direction = prev_direction
        else:
            print("*" * 50)
            print("valid direction lists")
            print("left, right, straight, back, none")
    print("draw.....")
    kkobo.pencolor(in_color)
    if in_direction == directions[0]:
        kkobo.left(90)
        kkobo.forward(in_distance)
    elif in_direction == directions[1]:
        kkobo.right(90)
        kkobo.forward(in_distance)
    elif in_direction == directions[2]:
        kkobo.forward(in_distance)
    elif in_direction == directions[3]:
        kkobo.back(in_distance)
    user_input = input("Please enter to start.....(exit to quit) >")
turtle.done()
