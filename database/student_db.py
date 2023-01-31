import sqlite3
from backend.student import Student

conn = sqlite3.connect('student.db')

c = conn.cursor()

c.execute(""" CREATE TABLE student (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  class TEXT NOT NULL,
  student_id TEXT UNIQUE NOT NULL,
  parent_id INTEGER NOT NULL,
  FOREIGN KEY (parent_id) REFERENCES Parent (id)
)  """)

# Instances of class
# note that we haven't inserted these into db

# student_1 = Student('John', 'Doe', 'olevels', '1003', 3)
# student_2 = Student('Kamal', 'Mustafa', 'alevels', '1004', 4)
#
# print(student_1.fullname)
# print(student_2.schoolinfo)

#c.execute("INSERT INTO student (first_name, last_name, student_class, student_id, parent_id) VALUES ('{}', '{}' , '{}', '{}','{}')".format(student_1.first_name, student_1.last_name, student_1.student_class, student_1.student_id, student_1.parent_id))

# c.execute("ALTER TABLE student RENAME COLUMN class TO student_class")


#c.execute("SELECT * FROM student")

#print(c.fetchall())
conn.commit()

conn.close()
