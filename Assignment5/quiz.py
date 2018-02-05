# Author : Joon Son
# Date : 17/Nov/2017
# Description :
# read multiple choice questions from csv file
# display question and get answer from the user
# calculate score as a percentage and display it

# pseudo code
# 1. open a file which has series of information regarding questions
# 2. iterate below code for each questions
# 3. count up value of numberofQ (number of question)
# 4. print question
# 5. print multiple choices with mark
# 6. get answer from the user with validity test
# 7. compare user input with the answer from the content
# 8. if the input is correct, count up a value of score
# 9. after end of quiz
# 10. if the number of questions is greater than zero
# 11. calculate percentage score
# 12. and print out the result

import csv
marks = ['a', 'b', 'c', 'd']  # list of marks for multiple choices
score = 0
numberOfQ = 0  # number of questions
QUIZ5 = "questions/questions_5.txt"
QUIZ3 = "questions/questions_3.txt"
ACCESS_READ = "r"

def get_anwer(str):
    # validity test
    # allow only [a, b, c, d]
    while True:
        result = input("Enter choice (a-d): ")
        if result not in marks:
            print("Invalid Input !!! ***Please enter choice (a, b, c, d)***")
            continue
        else:
            break
    return result

with open(QUIZ3, ACCESS_READ) as quizCSV:
    questions = csv.reader(quizCSV)
    for question in questions:
        numberOfQ += 1
        for i in range(len(question)-1):  # question + multiple choices
            if i == 0:  # position for question
                print(question[i])
            else:  # multiple choices
                print(marks[i-1]+") "+question[i])
        u_answer = get_anwer("Enter choice (a-d): ")  # get user answer
        if marks.index(u_answer) == int(question[len(question)-1]):
            score += 1
        print("")
    if numberOfQ > 0:
        score_per = score / numberOfQ * 100
        print("Your score is: {correct}/{total} ({percent:.1f}%)".format(correct=score, total=numberOfQ, percent=score_per))


