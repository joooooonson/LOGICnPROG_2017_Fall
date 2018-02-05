# Author: Joon Son
# Date: 2017-11-29
# Description: Nested 2D List challenge!
# use nested loop and create 2-D list


size = 0
character = "X"
shape = "box"


def drawing_box(size, character):
    side = size + size -1
    drawing = []
    for i in range(side):
        line = [" "] * side
        for j in range(side):
            if i == 0 or i == side-1:
                line[j] = character
            else:
                if j==0 or j==side-1:
                    line[j]=character
        drawing.append(line)
    return drawing

def drawing_diamond(size, character):
    side = size + size -1
    drawing = []
    for i in range(size):
        line = [" "]*side
        for j in range(side):
            cen = size - 1
            if j >= cen-i and j <=cen+i:
                line[j]=character
        drawing.append(line)
    for i in range(side - size):
        line = [" "] * side
        for j in range(side):
            if j>=i+1 and j<side-1-i:
                line[j]=character
        drawing.append(line)
    return drawing

while True:
    shape = input("Choose one of the shape box or diamond: ").lower()
    if shape != 'box' and shape != 'diamond':
        print("please choose a BOX or DIAMOND")
        continue
    else:
        break

while True:
    character = input("Enter one character to draw: ").upper()
    if len(character) != 1 and character.isprintable():
        print("please enter A CHARACTER")
        continue
    else:
        break

while True:
    try:
        size = int(input("Enter a number of size: "))
    except ValueError:
        print("Please enter a integer!!:")
        continue
    break


if shape == 'box':
    drawing = drawing_box(size, character)
elif shape == "diamond":
    drawing = drawing_diamond(size, character)

for line in drawing:
    for ch in line:
        print(ch,end=" ")
    print()





