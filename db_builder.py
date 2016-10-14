import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from os import path, remove
from sys import argv

f="discobandit.db"

debug = False
if len(argv) > 1 and argv[1] == "debugOn":
    debug = True
if debug and path.exists(f):
    remove(f)
    
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

try:
    with open('peeps.csv') as csvFile:
        peepsReader = csv.DictReader(csvFile)
        createStudentsTableQuery = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
        c.execute(createStudentsTableQuery)
        for row in peepsReader:
            insertStudentDataQuery = "INSERT INTO students VALUES ('"+ row['name'] + "'," + row['age'] + ',' + row['id'] + ')'
            c.execute(insertStudentDataQuery)

    with open('courses.csv') as csvFile:
        coursesReader = csv.DictReader(csvFile)
        createCoursesTableQuery = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"
        c.execute(createCoursesTableQuery)
        for row in coursesReader:
            insertCourseDataQuery = "INSERT INTO courses VALUES ('"+ row['code'] + "'," + row['mark'] + ',' + row['id'] + ')'
            c.execute(insertCourseDataQuery) 
except (OSError, IOError) as e:
    print "File not found..."
except (Exception) as e:
    print str(e)
    print "Unknown exception found"
    
#==========================================================

db.commit() #save changes
db.close()  #close database


