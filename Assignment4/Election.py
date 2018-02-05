# Author : Joon Son
# Date : 31/Oct/2017
# Description :
# Ask the user how many candidates are running in the current election,
# For each numbered candidate up to the user-entered count of candidates, allow the user to enter a name and
# the number of votes that person received.
# Calculate and output a list of all candidate names,
# Display what share of the total vote, as a percentage, that each candidate won,
# Highlight the candidate(s) with highest and lowest vote counts.

MSG_FIRST = "<--First Place"
MSG_LAST = "<--Last Place... HAHAHAHA"

# def get_positive_num(str):
#     # get user input as a integer
#     # check user input if it is numeric value or not
#     # if it is not numeric ask user enter again
#     # the input should be greater than 0
#
#     # list of numbers, to verify validity of input
#     NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#     while True:
#         input_valid = True
#         input_value = input(str)
#         for temp in input_value:
#             if temp not in NUMBERS:
#                 input_valid = False
#         if not input_valid:
#             print("Please Enter Integer Value")
#             continue
#         elif int(input_value) <= 0:
#             print("Please Enter Integer Value greater than zero")
#             continue
#         else:
#             break
#     return int(input_value)

def get_positive_num(str):
    # get user input as a integer
    # check user input if it is numeric value or not
    # if it is not numeric ask user enter again
    # the input should be greater than 0
    input_value = 0
    while(True):
        try:
            input_value = int(input(str))
        except ValueError:
            print("Please Enter Integer Value")
            continue
        else:
            if input_value <= 0:
                print("Please Enter Integer Value greater than zero")
                continue
            else:
                break
    return input_value


# get how many candidates are running in the current election

# sizeOfCandidates = int(input("Enter the number of candidates in the election : "))
sizeOfCandidates = get_positive_num("Enter the number of candidates in the election : ")
print("")

# list variable to store names and number of votes of candidates
candidates = []
# list variable to store sum of numbers of votes of candidates
listVotes = []
totalVotes = 0
for i in range(sizeOfCandidates):
    name = input("Enter the name of candidate #{}: ".format(i+1))
    # votes = int(input("Enter the number of votes for candidate {}: ".format(i+1)))
    nbrvotes = get_positive_num("Enter the number of votes for candidate {}: ".format(i+1))
    # list variable to store name and number of votes of one candidate
    candidate = [name, nbrvotes]
    # add to votes
    totalVotes += nbrvotes
    # append to candidate list
    candidates.append(candidate)

# append share of total votes as a percentage that each candidate won
for i in range(sizeOfCandidates):
    candidates[i].append((candidates[i][1] / totalVotes) * 100)


# find maximum value of number of votes and minimum value of number of votes\
maxVotes = 0
minVotes = totalVotes

for candidate in candidates:
    if candidate[1] > maxVotes:
        maxVotes = candidate[1]

    if candidate[1] < minVotes:
        minVotes = candidate[1]

# append place information to each candidate list variable

for i in range(sizeOfCandidates):
    if candidates[i][1] == maxVotes:
        candidates[i].append(MSG_FIRST)
    elif candidates[i][1] == minVotes:
        candidates[i].append(MSG_LAST)
    else:
        candidates[i].append(" ")


print("\nElection result")
print("-"*50)

# print the result of election
for candidate in candidates:
    print("{name:10}\t - {votes:.1f}% {message}".format(name=candidate[0], votes=candidate[2], message=candidate[3]))
    # print(candidate[0]+" \t\t - {:.1f}%  ".format(candidate[2]) + candidate[3])


