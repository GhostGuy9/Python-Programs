import os
#Please don't change this file

os.system('cls')
folder = ""

#Lists what is in the MadLib Folder
print("List of MadLibs:")
for x in os.listdir('madlibs/'):
    print(x)

#Ends List
print("--------------------")

#User Input
folder = input("What Madlib would you like to try?: ")
os.system(f"python madlibs/{folder}/questions.py")

#print(story)
again = input("Continue press enter")
