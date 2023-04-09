import sqlite3 as db
from backend.student import Student

conn = db.connect('student.db')

c = conn.cursor()


c.execute(""" CREATE TABLE verificationevent (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date TEXT NOT NULL,
  time TEXT NOT NULL,
  student_id TEXT UNIQUE NOT NULL,
  parent_id INTEGER NOT NULL,
  FOREIGN KEY (parent_id) REFERENCES parent (id)
  FOREIGN KEY (first_name) REFERENCES parent (student_name)
)  """)

#Instances of class

student_1 = Student('John','Doe', 'olevels','1003', 3)
student_2 = Student('Zayd','Youssef', 'alevels','1004', 4)

print(student_1.fullname)



#c.execute("INSERT INTO student (first_name, last_name, student_class, student_id, parent_id) VALUES (:fname, :lastname, :classid, :id, :parentid)".format(student_1.first_name, student_1.last_name, student_1.student_class,student_1.student_id, student_1.parent_id))

c.execute("SELECT * FROM student")
print(c.fetchall())

conn.commit()

conn.close()