'''Sascha Gordon-Zolov
Team Sizzle
Softdev
K04:: Python Dictionaries and Random Selections
2024-9-17
Time spent: '''
import random
def bitstream():
    file = open("krewes.txt", "r")
    file = file.read()
    l1 = file.split("@@@")
    for i in range (0, len(l1) - 1):
        l1[i] = l1[i].split("$$$")
    r = random.randint(0, len(l1) - 1)
    return ("Period: " + l1[r][0] + ", Name: " + l1[r][1] + ", Ducky: " + l1[r][2])

print(bitstream())