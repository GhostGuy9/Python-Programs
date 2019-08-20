import os
#Configure this Section
questions = [
    "Type a Adverb",
    "Type a Verb",
    "Type a Verb in Past Tense",
    "Type a Adjective",
    "Type a Plural Noun",
    "Fictional Character Name",
    "Type a undesirable Noun",
    "Type a Verb",
    "Type a Noun",
    "Type a Verb in Past Tense ending in \"S\"",
    "Type a Plural Noun",
    "Enter a Number(0 or Zero)",
    "Type a Plural Noun",
    "Type a Adjective",
    "Type a Adjective",
    "Type a Noun"
]
question_type = [
    "Adverb",
    "Verb",
    "Verb",
    "Adjective",
    "Noun",
    "Character",
    "Noun",
    "Verb",
    "Noun",
    "Verb",
    "Noun",
    "Number",
    "Noun",
    "Adjective",
    "Adjective",
    "Noun"
]
num_of_questions = 16

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

#Shows Story by clearing screen
story = open("madlibs/Catcher/madlib.txt").read().format(answers=answers)
os.system('cls')
print(f"Catcher in the {answers[6]}")
print("-----------")
print(story)
print()
