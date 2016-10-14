import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...
d1 = csv.DictReader(open('peeps.csv'))
d2 = csv.DictReader(open('courses.csv'))


q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
c.execute(q)

for row in d1:
    q = "INSERT INTO students VALUES ('"+ row['name'] + "'," + row['age'] + ',' + row['id'] + ')'
    #print q
    c.execute(q)

q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
c.execute(q)
for row in d2:
    q = "INSERT INTO courses VALUES ('"+ row['code'] + "'," + row['mark'] + ',' + row['id'] + ')'
    c.execute(q)    
    

'''
q = "CREATE TABLE students (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query


q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)
'''

#==========================================================
db.commit() #save changes
db.close()  #close database


