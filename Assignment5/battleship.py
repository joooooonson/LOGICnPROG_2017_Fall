# Author : Joon Son
# Date : 17/Nov/2017
# Description : simple battle ship game
# start main logic from here

# pseudo code
# 1. make 2-d list which contains the positions of targets from the file
# 2. draw initial showing map
# 3. print welcome message
# 4. iterate below code until when the number of remain missiles is equal
#       to zero or scores user got is equal to total number of target
# 5. print showing map on screen
# 6. ask user input the place of target
# 7. evaluate weather the input is correct or not
# 8. update showing map, if the input is correct, O would be replaced at that position
#       if the input is wrong, X would be replaced at that position
# 9. if the input is right, print "HIT!!!!!!" and count up the value of scores
# 10. otherwise, print "MISS"
# 11. if the value of score is equal to the number of total target,
#       print congratulation message and result
# 12 otherwise reduce one from the number of remain missiles and print the result
#  and if the value of remains is equal to zero, print game over message and the result
#
import csv
PARH_TARGETMAP = "BattleshipSampleApp/map.txt"
ACCESS_READ = "r"
SIZE_X = 11
SIZE_Y = 11
MISSILES = 30
HIT = "O"
MISS = "X"

remains = MISSILES
scores = 0
tot_targets = 0
cols = "ABCDEFGHIJ"  # columns marks
rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  # row marks
map_display = [[" " for x in range(SIZE_X)] for y in range(SIZE_Y)]
map_target = []

def init_map_target():
    # create 2-d list of targets-map from the content for the file
    # return total number of targets
    numberOftargets = 0  # total number of targets
    with open(PARH_TARGETMAP, ACCESS_READ) as map_csv:
        targets_file = csv.reader(map_csv)
        for row in targets_file:
            row_list = []
            for target in row:
                row_list.append(target)
                if target == "1":  # if it is target
                    numberOftargets += 1  # count up number of target
            map_target.append(row_list)
    return numberOftargets


def init_map_display():
    # draw initial target map
    #   A  B  C  D  E  F  G  H  I  J
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    for x in range(SIZE_X):
        for y in range(SIZE_Y):
            if x == 0 and y > 0:
                map_display[x][y] = cols[y-1]  # A B C D E F G H I J
            elif y == 0 and x > 0:
                map_display[x][y] = rows[x-1]  # 1 2 3 4 5 6 7 8 9 10
            else:
                map_display[x][y] = ""


def show_map_display():
    # print showing map on screen   SIZE_X x SIZE_Y 2-d list
    for x in range(SIZE_X):
        for y in range(SIZE_Y):
            print("{:>2}".format(map_display[x][y]), end="")
        print("")


def get_guess(in_str):
    # validate user input
    # the input should be [A~J][1~10]
    result = {"col": 0, "row": 0}
    while True:
        u_input = input(in_str)
        try:
            if u_input[0].upper() not in cols or u_input[1:] not in rows :
                print("Not valdate input!!! (Ex A1)")
                continue
            else:
                col = cols.index(u_input[0].upper())
                row = rows.index(u_input[1:])
                result["col"] = col
                result["row"] = row
                break
        except IndexError:
            print("Not valdate input!!! (Ex A1)")
            continue
    return result


def eval_hit(position):
    # check weather the user input hit a target or not
    result = MISS
    if map_target[position["row"]][position["col"]] == "1":
        result = HIT

    return result



tot_targets = init_map_target()
init_map_display()
print("Let's play Battleship!")
print("You have {} missiles to fire to sink all five ships.\n".format(MISSILES))
while remains != 0 and scores != tot_targets:
    show_map_display()
    guess = get_guess("Choose your target (Ex.A1): ")
    hit = eval_hit(guess)
    map_display[guess["row"]+1][guess["col"]+1] = hit

    if hit == HIT:
        print("HIT!!!!!")
        scores += 1
    else:
        print("MISS")

    if scores == tot_targets:
        print("YOU SANK MY ENTIRE FLEET!!")
        print("You had {scores} of {total} hits, which sank all the ships!".format(scores = scores, total = tot_targets))
        show_map_display()
        print("You won, congratulation!")
    else:
        remains -= 1
        print("You have {} missiles remaining".format(remains))
        if remains == 0:
            print("GAME OVER")
            print("You had {scores} of {total} hits, but didn\'t sink all the ships...".format(scores = scores, total = tot_targets))
            print("Better luck next time")
