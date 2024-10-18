import csv
import sqlite3

with open('students.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    db = sqlite3.connect("foo")
    c = db.cursor()
    #c.execute("CREATE TABLE roster(name TEXT, userid INTEGER, age INTEGER)")
    for line in reader:
        c.execute("INSERT INTO roster (name, userid, age) VALUES (line[("name")], line[("userid")], line[("age")])")
    db.commit()
    db.close()
