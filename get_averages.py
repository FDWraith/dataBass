#!/usr/bin/python

import sqlite3

filename = "discobandit.db"

database = sqlite3.connect(filename)
cursor = database.cursor()

try:
    getStudentDataCmd = "SELECT name, mark, students.id FROM students, courses WHERE students.id == courses.id"
    cursor.execute(getStudentDataCmd)
    studentsGrade = {}
    studentsNumCourses = {}
    studentsIDs = {}
    for row in cursor:
        studentName = row[0]
        studentGrade = row[1]
        studentID = row[2]
        print studentName, studentGrade
        if studentName not in studentsIDs:
            studentsIDs[studentName] = studentID
        if studentName in studentsGrade:
            studentsGrade[studentName] += studentGrade
            studentsNumCourses[studentName] += 1
        else:
            studentsGrade[studentName] = studentGrade
            studentsNumCourses[studentName] = 1
    print "-------------------------------------------------------"
    studentsAverage = {}
    for name in studentsGrade:
        studentAvg = float(studentsGrade[name]) / studentsNumCourses[name]
        studentID = studentsIDs[name]
        studentsAverage[name] = studentAvg
        print "Student: %s, ID: %d, Avg: %d" % (name, studentID, studentAvg)
except Exception as e:
    print "Corrupted Database..."
