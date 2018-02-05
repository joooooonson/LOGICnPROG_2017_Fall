# Author : Joon Son
# Date : 31/Oct/2017
# Description :
# Take a sentence or phrase as input,
# Count the number of occurrences of each vowel in the user-entered sentence, regardless of case sensitivity,
# Display the counts per vowel to the user,
# The program will keep asking the user to enter a new sentence until the user enters the command ‘quit’.

# list of vowels
VOWELS = ['A', 'E', 'I', 'O', 'U']

# get a sentence or phrase as input from user and convert all to uppercase
inPhrase = input("Type a phrase (or quit ot exit program) : ").upper()
print("")
# until user input quit, iterates below code
while inPhrase != "QUIT":
    # list variable to store count
    count = [0, 0, 0, 0, 0]
    # if a character in the input is one of vowels, count up
    for i in range(len(inPhrase)):
        if inPhrase[i] in VOWELS:
            for j in range(len(VOWELS)):
                if inPhrase[i] == VOWELS[j]:
                    # count up
                    count[j] = count[j]+1

    # print number of each vowel
    for i in range(len(VOWELS)):
        print("Letter " + VOWELS[i] + " count: {}".format(count[i]))
    print("")
    # get a sentence or phrase as input from user and convert all to uppercase again
    inPhrase = input("Type a phrase (or quit ot exit program) : ").upper()
    print("")


