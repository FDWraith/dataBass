import sqlite3

db = sqlite3.connect("discobandit.db")
cursor = db.cursor()

cmd = "SELECT mark, name FROM students, courses WHERE students.id == courses.id"
selection = cursor.execute(cmd)
cmd = "SELECT name FROM students"
selection2 = cursor.execute(cmd)

for record in selection2:
    for row in selection:
        if(row[1] == record):
            

