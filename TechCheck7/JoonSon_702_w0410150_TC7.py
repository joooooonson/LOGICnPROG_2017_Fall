"""
    Roll the Dice:

    This program simulates the rolling of 5 dice by generating five random numbers.
    It will display the numbers as dice
    to the console, then will determine based on those numbers the highest value combination
    that was rolled.
    It should account for the following combination possibilities:

        0 - No Combination (e.g. 1 2 3 5 6)

        1 - One Pair (e.g. 2 3 3 5 6)

        2 - Two Pair (e.g. 2 2 5 6 6)

        3 - Three of a kind (e.g. 2 4 4 4 6)

        4 - Small straight(4 in a row) (e.g. 1 3 4 5 6)

        5 - Large straight(5 in a row) (e.g. 1 2 3 4 5)

        6 - Full House (Three of a kind + one pair) (e.g. 4 4 6 6 6)

        7 - Four of a kind (e.g. 2 5 5 5 5)

        8 - Five of a kind (e.g. 4 4 4 4 4)
"""
import random


# This function will simply "roll the dice" and return the value rolled.
# For testing purposes the function takes a die value with a default value and "rolls the die" if the parameter is not
# passed. That way we can hard-code and pass in parameters for testing purposes.

# author : joon son
# date : 3/Nov/2017
# modified:
# add two function (check_for_small_straight, check_for_large_straight)

def roll_dice(die_value=0):

    # If no value for the die is passed in, we call random int for a number between 1 and 6 and set it as the result
    # otherwise, set the result to the number passed in
    if die_value == 0:
        result = random.randint(1, 6)
    else:
        result = die_value

    return result


# This function will update the count, for each possible result
def determine_value_count(target_value, die1, die2, die3, die4, die5):
    total = 0

    if die1 == target_value:
        total += 1
    if die2 == target_value:
        total += 1
    if die3 == target_value:
        total += 1
    if die4 == target_value:
        total += 1
    if die5 == target_value:
        total += 1

    return total


# TODO: CREATE A FUNCTION HERE TO CHECK FOR A SMALL STRAIGHT
def check_for_small_straight(die1, die2, die3, die4, die5):
    # list variable for dies
    dies = [die1, die2, die3, die4, die5]
    # set initial value as False
    result = False

    for i in range(5):
        # choose 4items in the list and check whether they are in a row or not
        cnt_next = 0  # variable for indicating number of pairs of adjacent numbers
        temp = dies[i]  # before deleting save the value in temp variable
        del dies[i]  # delete one item
        dies.sort()  # sort list ascending order
        for j in range(1, 4):  # iterates from 1 to 3
            if dies[j-1] + 1 == dies[j]:  # when they are next to each other
                cnt_next = cnt_next + 1  # increase the value of cnt_next
        if cnt_next == 3:  # if the number the adjacent pairs is 3
            result = True  # this list is in small straight
        dies.insert(i, temp)  # recover the deleted value
    return result


# TODO: CREATE A FUNCTION HERE TO CHECK FOR A LARGE STRAIGHT
def check_for_large_straight(die1, die2, die3, die4, die5):
    # list variable for dies
    dies = [die1, die2, die3, die4, die5]
    # set initial value as False
    result = False
    cnt_next = 0  # variable for indicating number of pairs of adjacent numbers
    dies.sort()  # sort list ascending order
    for i in range(1, 5): # iterates from 1 to 4
        if dies[i-1] + 1 == dies[i]:  # when they are next to each other
            cnt_next = cnt_next + 1  # increase the value of cnt_next
    if cnt_next == 4:  # if the number the adjacent pairs is 3
        result = True  # this list is in large straight
    return result


# This function returns an integer representing the type of combination that was determined
def get_highest_combination(die1, die2, die3, die4, die5):

    # variables to store the count of each value rolled
    ones_count = 0
    twos_count = 0
    threes_count = 0
    fours_count = 0
    fives_count = 0
    sixes_count = 0

    result = 0  # means no combination

    # now update all of the counts accordingly
    ones_count = determine_value_count(1, die1, die2, die3, die4, die5)
    twos_count = determine_value_count(2, die1, die2, die3, die4, die5)
    threes_count = determine_value_count(3, die1, die2, die3, die4, die5)
    fours_count = determine_value_count(4, die1, die2, die3, die4, die5)
    fives_count = determine_value_count(5, die1, die2, die3, die4, die5)
    sixes_count = determine_value_count(6, die1, die2, die3, die4, die5)

    if ones_count == 5 or twos_count == 5 or threes_count == 5 or fours_count == 5 or fives_count == 5 or \
                    sixes_count == 5:
        # this means we have five of a kind
        result = 8
    elif ones_count == 4 or twos_count == 4 or threes_count == 4 or fours_count == 4 or fives_count == 4 or \
                    sixes_count == 4:
        # this means we have four of a kind
        result = 7
    elif ones_count == 3 or twos_count == 3 or threes_count == 3 or fours_count == 3 or fives_count == 3 or \
                    sixes_count == 3:
        # this means we have at least three of a kind
        # assume just a three of a kind
        result = 3

        # then must check for full house, which we will recall is better than just three of a kind
        if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fives_count == 2 or \
                        sixes_count == 2:
            # full house
            result = 6
    elif ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fives_count == 2 or \
                    sixes_count == 2:
        # we have at least a pair - assume a pair
        result = 1

        # need to check for two pair or small straight, which are both better than just one pair
        # check for two pair first
        if ones_count == 2:
            if twos_count == 2 or threes_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:
                # we have two pair
                result = 2
        elif twos_count == 2:
            if ones_count == 2 or threes_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:
                # we have two pair
                result = 2
        elif threes_count == 2:
            if ones_count == 2 or twos_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:
                # we have two pair
                result = 2
        elif fours_count == 2:
            if ones_count == 2 or twos_count == 2 or threes_count == 2 or fives_count == 2 or sixes_count == 2:
                # we have two pair
                result = 2
        elif fives_count == 2:
            if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or sixes_count == 2:
                # we have two pair
                result = 2
        elif sixes_count == 2:
            if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fives_count == 2:
                # we have two pair
                result = 2
        # do we have a small straight?
        # TODO: CALL FUNCTION TO CHECK FOR A SMALL STRAIGHT HERE AND SET RESULT TO 4 IF TRUE
        if check_for_small_straight(die1, die2, die3, die4, die5):
            result = 4
    else:
        result = 0
        # check for large and small straight if no pairs
        # TODO: CALL FUNCTION TO CHECK FOR A LARGE STRAIGHT HERE AND SET RESULT TO 5 IF TRUE
        if check_for_large_straight(die1, die2, die3, die4, die5):
            result = 5
        # TODO: CALL FUNCTION TO CHECK FOR A SMALL STRAIGHT HERE AND SET RESULT TO 4 IF TRUE
        elif check_for_small_straight(die1, die2, die3, die4, die5):
            result = 4

    return result


# initialize some local variables
die_one_name = "Dice 1"
die_two_name = "Dice 2"
die_three_name = "Dice 3"
die_four_name = "Dice 4"
die_five_name = "Dice 5"


# simulates the rolling of 5 dice by generating five random numbers - USE THIS CODE BLOCK FOR RANDOM DICE ROLLS
die_one_value = roll_dice()
die_two_value = roll_dice()
die_three_value = roll_dice()
die_four_value = roll_dice()
die_five_value = roll_dice()

# hard-codes the dice values for testing purposes - FOR TESTING - WAITING FOR A FULL HOUSE RANDOMLY CAN BE PAINFUL
# die_one_value = roll_dice(3)
# die_two_value = roll_dice(2)
# die_three_value = roll_dice(6)
# die_four_value = roll_dice(5)
# die_five_value = roll_dice(4)

# Output each die result
print("{0}: {1}".format(die_one_name, die_one_value))
print("{0}: {1}".format(die_two_name, die_two_value))
print("{0}: {1}".format(die_three_name, die_three_value))
print("{0}: {1}".format(die_four_name, die_four_value))
print("{0}: {1}".format(die_five_name, die_five_value))


# determine and output highest combination
highest_combo = get_highest_combination(die_one_value, die_two_value, die_three_value, die_four_value, die_five_value)
highest_combo_as_string = ""

if highest_combo == 8:
    highest_combo_as_string = "Five of a Kind"
elif highest_combo == 7:
    highest_combo_as_string = "Four of a Kind"
elif highest_combo == 6:
    highest_combo_as_string = "Full House"
elif highest_combo == 5:
    highest_combo_as_string = "Large Straight"
elif highest_combo == 4:
    highest_combo_as_string = "Small Straight"
elif highest_combo == 3:
    highest_combo_as_string = "Three of a Kind"
elif highest_combo == 2:
    highest_combo_as_string = "Two Pair"
elif highest_combo == 1:
    highest_combo_as_string = "One Pair"
elif highest_combo == 0:
    highest_combo_as_string = "No Combination"
else:
    highest_combo_as_string = "System Error"

print("Highest Combination: {}".format(highest_combo_as_string))
