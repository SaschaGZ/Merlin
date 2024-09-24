'''Sascha Gordon-Zolov
Team Sizzle
Softdev
K06: Python csv reading and dictionaries
2024-9-20
Time spent: 1.5'''
import csv
import random
def numbercruncher():
    with open("occupations.csv", "r") as file:
        next(file)
        f = csv.reader(file)
        dic = {}
        for i in f:
            dic.update({i[0]: float(i[1])})
        total = dic["Total"]
        key = dic.keys()
        for k in key:
            num = dic[k]
            if (num / total) > random.random(): #random.random generates a float in (0, 1)
                return k
            else:
                total -= num #Used for weighted probability; subtracts the probability from the total if the occupation is not chosen
print(numbercruncher())
        