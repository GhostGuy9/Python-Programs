import os

#Configure this Section
questions = [
    "Describe the time of day outside",
    "A Adjective for something good",
    "A Type of Bird",
    "Room in a house",
    "A Past-Tense Verb",
    "A Verb for traveling",
    "Relative's Name or Parent",
    "A Noun that be consumed",
    "A liquid of any kind",
    "Verb ending in -ing",
    "Body Part on yourself",
    "A Plural Noun",
    "Verb ending in -ing",
    "A object that can fit in a room"
]
question_type = [
    "Adj",
    "Adj",
    "Object",
    "Room",
    "Verb",
    "Verb",
    "Name",
    "Noun",
    "Object",
    "Verb",
    "Object",
    "Noun",
    "Verb",
    "Noun"
]
num_of_questions = 14

#For Loop - Don't Touch or Do, Full customizable stuff here
answers = []
question_num = 0
question = 0
debug = 0

#Question Loop - Don't Touch or you might break it.
while num_of_questions > question_num and debug == 0:
    os.system('cls')
    question_num = question_num+1
    print(f"Question {question_num} of {num_of_questions}")
    answer = input(question_type[question] + " | " + questions[question]+ ": ")
    answers.insert(question, answer)
    question = question + 1

while num_of_questions > question_num and debug == 1:
    os.system('cls')
    question_num = question_num+1
    print(f"Question {question_num} of {num_of_questions}|Index: {question}")
    answer = input(question_type[question] + " | " + questions[question]+ ": ")
    answers.insert(question, answer)
    question = question + 1
#End of Question Loop - Don't Touch or you might break it.

#Shows Story by clearing screen and showing title and story.
story = open("madlibs/November/madlib.txt").read().format(answers=answers)
os.system('cls')

#Title - Customize
print(f"A {answers[0]} November Morning!")
print("-----------")
print(story)
print()
