#Roll the Dice:

#This program simulates the rolling of 5 dice by generating five random numbers.
#It will display the numbers as dice
#to the console, then will determine based on those numbers the highest value combination
#that was rolled. It should account for the following combination possibilities:
# No combination(12345,12346,12356,)
# 1 - One pair(11/22/33/44/55/66 *
# 2- two pair
# 3 - Three of a kind
# 4- small straight(4 in a row)
# 5 - Large straight(5 in a row)
# 6 - Full house
# 7 - Four of a kind
# 8 - Five of a kind

import random

def roll_dice(die_value=0):

    if die_value == 0:
        result = random.randint(1, 6)
    else:
        result = die_value

    return result

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

    return

def check_for_small_straight(die1, die2, die3, die4, die5):

    dies = [die1, die2, die3, die4, die5]

    for i in range(5):

        cnt_next = 0
        temp = dies[i]
        del dies [i]
        dies.sort()
        for j in range(0,3):
            if dies[j]+1 == dies[j+1]:
                cnt_next = cnt_next + 1
        if cnt_next == 3:
            result = True
        dies.inser(i, temp)
    return result

def check_for_large_straigt(die1, die2, die3, die4, die5):

    dies = [die1, die2, die3, die4, die5]

    for i in range(5):

        cnt_next = 0
        temp = dies[i]
        del dies [i]
        dies.sort()
        for j in range(0,4):
            if dies[i]+1 == dies[i+1]:
                cnt_next = cnt_next+ 1
        if cnt_next == 4:
            result = True
        return result

def get_highest_combination(die1, die2, die3, die4, die5):

    ones_count =0
    twos_count = 0
    threes_count = 0
    fours_count = 0
    fives_count = 0
    sixes_count = 0

    result = 0

    ones_count = determine_value_count(1, die1, die2, die3, die4, die5)
    twos_count = determine_value_count(2, die1, die2, die3, die4, die5)
    threes_count = determine_value_count(3, die1, die2, die3, die4, die5)
    fours_count = determine_value_count(4, die1, die2, die3, die4, die5)
    fives_count = determine_value_count(5, die1, die2, die3, die4, die5)
    sixes_count = determine_value_count(6, die1, die2, die3, die4, die5)

    if ones_count == 5 or twos_count == 5 or threes_count == 5 or fours_count == 5 or fours_count == 5 or fives_count == 5 or sixes_count == 5:

        result = 8

    elif ones_count == 4 or twos_count == 4 or threes_count == 4 or fours_count == 4 or fours_count == 4 or fives_count == 4 or sixes_count == 4:

        result = 7

    elif ones_count == 3 or twos_count == 3 or threes_count == 3 or fours_count == 3 or fours_count == 3 or fives_count == 3 or sixes_count == 3:

        result = 3

        if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:

            result = 6

    elif ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:

        result =1

    if ones_count == 2:
        if twos_count == 2 or threes_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:

            result = 2
    elif twos_count == 2:
        if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:
            result = 2

    elif threes_count == 2:
        if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:
            result = 2

    elif fours_count == 2:
       if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:
           result = 2

    elif fives_count == 2:
        if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:
            result = 2

    elif sixes_count == 2:
        if ones_count == 2 or twos_count == 2 or threes_count == 2 or fours_count == 2 or fours_count == 2 or fives_count == 2 or sixes_count == 2:
            result = 2

    if check_for_small_straight(die1, die2, die3, die4, die5):
        result = 4

    else:
        reslut = 0

        if check_for_large_straigt(die1, die2, die3, die4, die5):
            result = 5

        elif check_for_small_straight(die1, die2, die3, die4, die5):
            result = 4

    return result



die_one_name = "Dice 1"
die_two_name = "Dice 2"
die_three_name = "Dice 3"
die_four_name = "Dice 4"
die_five_name = "Dice 5"

die_one_value = roll_dice()
die_two_value = roll_dice()
die_three_value = roll_dice()
die_four_value = roll_dice()
die_five_value = roll_dice()

print("{0}: {1}".format(die_one_name, die_one_value))
print("{0}: {1}".format(die_two_name, die_two_value))
print("{0}: {1}".format(die_three_name, die_three_value))
print("{0}: {1}".format(die_four_name, die_four_value))
print("{0}: {1}".format(die_five_name, die_five_value))

highest_combo = get_highest_combination(die_one_value, die_two_value, die_three_value, die_four_value, die_five_value)
highest_combo_as_string = ""

if highest_combo == 8:
    highest_combo_as_string = "Five of a kind"
elif highest_combo == 7:
    highest_combo_as_string = "Four of a kind"
elif highest_combo == 6:
    highest_combo_as_string = "Full House"

elif highest_combo == 5:
    highest_combo_as_string = "Large straight"

elif highest_combo == 4:
    highest_combo_as_string = "Small straight"

elif highest_combo == 3:
    highest_combo_as_string = "Three of a kind"

elif highest_combo == 2:
    highest_combo_as_string = "Two of a kind"

elif highest_combo == 1:
    highest_combo_as_string = "One of a kind"

elif highest_combo == 0:
    highest_combo_as_string = "No Combination"

print("Highest combination: {}".format(highest_combo_as_string))