'''Sascha Gordon-Zolov
Team Sizzle
Softdev
K04:: Python Dictionaries and Random Selections
2024-9-17
Time spent: 0.5'''
import random
def bitstream():
    file = open("krewes.txt", "r") #r is read
    file = file.read()
    l1 = file.split("@@@") #single array
    for i in range (0, len(l1) - 1):
        l1[i] = l1[i].split("$$$") #double array
    r = random.randint(0, len(l1) - 1)
    print(l1)
    return ("Period: " + l1[r][0] + ", Name: " + l1[r][1] + ", Ducky: " + l1[r][2])

print(bitstream())