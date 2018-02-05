# Author : Joon Son
# Date : 16/Nov/2017
# Description :
# 1. read a text file
# 2. display the text from the file on-screen
# 3. make alterations to the file
#   -1 add a line number
#   -2 randomly select a line in the file and convert it to all capital letters
#   -3 Every other lines should be converted to all lowercase letters
# 4. display the altered text to the console
# 5. save it as a new text file

# pseudo code
# 1> open the file and create file object
# 2> find(move to) a end position
# 3> find(move to) a cur position
# 4> until the end of the file read a each line of content from the file
# 5> append the line to list
# 6> Display origin text
# 5> get a random number
# 6> iterates below codes until end of the list#
# 7> add a line number
# 8> convert the line to upper case whose index number is equal to the random number
# 8> convert every other lines to lower case
# 8> display altered text on-screen
# 9> save the altered text to new file
# 10> close every file object
import random

PATH_ORIGIN = "textfiles/AManNamedJed.txt"
PATH_ALTERED = "textfiles/new_file.txt"
ACCESS_READ = "r"
ACCESS_WRITE = "w"
content_lines = []
content_text = ""
cur_position = 0
end_position = 0
numberoflines = 0
upper_line = 0

# open the file and create file object
try:
    man_jed = open(PATH_ORIGIN, ACCESS_READ)
except FileNotFoundError:
    print("Could not find the file . . . . ")

# find a end position
man_jed.seek(0, 2)
end_position = man_jed.tell()

# find a cur position
man_jed.seek(0, 0)
cur_position = man_jed.tell()

# until the file pointer hit the end of the file
while cur_position != end_position:
    # read a line from the file
    line_str = man_jed.readline()
    # append th line to list
    content_lines.append(line_str)
    # update the value of current position
    cur_position = man_jed.tell()

# Display origin text
print("-"*50)
print("Original Text")
print("-"*50)
for content_line in content_lines:
    print(content_line,end="")
print("\n\n")

# get the number of lines
numberoflines = len(content_lines)

# randomly choose a line to be converted to uppercase
upper_line = random.randint(0,numberoflines-1)

# make alterations
for i in range(numberoflines):
    # add a line number
    content_lines[i] = str(i+1)+": "+content_lines[i]

    # convert the chosen line to upper case
    if i == upper_line:
        content_lines[i] = content_lines[i].upper()
    else:
        content_lines[i] = content_lines[i].lower()

# display altered text on-screen
print("-"*50)
print("Altered Text")
print("-"*50)
for content_line in content_lines:
    print(content_line,end="")
print("\n\n")

# save the altered text to new file
new_file = open(PATH_ALTERED, ACCESS_WRITE)
for content_line in content_lines:
    new_file.write(content_line)

# close file object
new_file.close()
man_jed.close()