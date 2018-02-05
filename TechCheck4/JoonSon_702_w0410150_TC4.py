# name : Joon Son
# date : 06/Oct/2017
# description : fix errors 1. "==" -> "="
#                          2. ":.0f" -> ":.1f"

# rename variables appropriately
InvalidCnt = 1  # rename c -> InvalidCnt

LetterGrade = ""  # rename l -> LetterGrade
UserInput = ""  # rename u -> UserInput
MarkLetter = ""  # rename m -> MarkLetter
NumericGrade = 0  # rename n-> NumericGrade

# list of valid letter grades
ValidLetterGrades = ["A", "B", "C", "D", "E", "F"]  # rename vls -> ValidLetterGrades
# list of valid mark letters
ValidMarkLetters = ["+", "-", ""]  # rename vms -> ValidMarkLetters

# iterate below code until the value of LetterGrade has one of values in ValidLetterGrades or
# the value of MarkLetter has one of values in ValidMarkLetters
while LetterGrade not in ValidLetterGrades or MarkLetter not in ValidMarkLetters:
    # when the value of InvalidCnt is bigger than 1, print message "You must enter a valid letter grade!"
    if InvalidCnt > 1:
        print("You must enter a valid letter grade!")
    # get letter grade from user and convert to upper case and assign it to UserInput
    UserInput = input("Enter a letter grade: ").upper()

    # when letter grade user input is not blank and the length of input is less than or equal to 2
    # set the first letter of input to LetterGrade
    if UserInput != "" and len(UserInput) <= 2:
        LetterGrade = UserInput[0]
        # when the length of input is equal to 2 and the first letter is not 'F'
        # set the second letter of input to MarkLetter
        if len(UserInput) == 2 and LetterGrade != "F":
            MarkLetter = UserInput[1]
        # when just the length of input is equal to 2,
        # set 'x' to MarkLetter
        elif len(UserInput) == 2:
            MarkLetter = "x"
        # otherwise, set MarkLetter as blank
        else:
            MarkLetter = ""

    # error!! fix '==' -> '='
    # InvalidCnt == InvalidCnt + 1

    # add 1 to InvalidCnt
    InvalidCnt = InvalidCnt + 1

# When the value of LetterGrade is equal to 'A', assign 4 to NumericGrade
if LetterGrade == "A":
    NumericGrade += 4
# When the value of LetterGrade is equal to 'B', assign 3 to NumericGrade
elif LetterGrade == "B":
    NumericGrade += 3
# When the value of LetterGrade is equal to 'C', assign 2 to NumericGrade
elif LetterGrade == "C":
    NumericGrade += 2
# When the value of LetterGrade is equal to 'D', assign 1 to NumericGrade
elif LetterGrade == "D":
    NumericGrade += 1

# When the value of MarkLetter is equal to "+" and the value of LetterGrade is not "A",
# add 0.3 to NumericGrade
if MarkLetter == "+" and LetterGrade != "A":
    NumericGrade += 0.3
# When the value of MarkLetter is equal to "-"
# subtract 0.3 to NumericGrade
elif MarkLetter == "-":
    NumericGrade -= 0.3
# error!! fix :.0f -> :.1f
# print("The numeric value is {0:.0f}".format(NumericGrade))
print("The numeric value is {0:.1f}".format(NumericGrade))
