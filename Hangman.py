# first we give computer 3 names out of which it chooses one and we guess its number of letters
import random

print('Welcome to hangman !!')
list1 = ["resonance", "motion ", "hello" , "ramesh" , "mukesh" , "suresh", "elon" , "mark" ]
list2 = str(random.choice(list1))
character = len(list2)
temp = ""
final = ""

# h = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']
for i in range(len(list2)):
    final+="_"
for step in range(character):
    l1 = str(input('Please enter a letter\n')).lower()
    for letter in list2:
        if letter == l1:
            temp+=l1
        else:
            temp+="_"
    ballesh = ""
    for i in range(len(temp)):
        if final[i]=="_" and temp[i]!="_":
            ballesh+=temp[i]
        elif final[i]!="_" and temp[i]=="_":
            ballesh+=final[i]
        else:
            ballesh+="_"
            # print(h[step])
    final = ballesh
    temp=""
    print(final)




