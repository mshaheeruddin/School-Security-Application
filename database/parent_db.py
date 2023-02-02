import sqlite3 as db


conn = db.connect('parent.db')

c = conn.cursor()


c.execute(""" CREATE TABLE parent (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  parent_name TEXT NOT NULL,
  student_name TEXT NOT NULL,
  relationship TEXT NOT NULL,
  phone_number TEXT UNIQUE NOT NULL,
  vehicle_number TEXT,
  vehicle_type  TEXT
)  """)

#Instances of class

#student_1 = Student('John','Doe', 'olevels','1003', 3)
#student_2 = Student('Zayd','Youssef', 'alevels','1004', 4)

#print(student_1.fullname)



#c.execute("INSERT INTO parent (parent_name, student_name, relationship, phone_number, vehicle_number, vehicle_) VALUES (:fname, :lastname, :classid, :id, :parentid)".format(student_1.first_name, student_1.last_name, student_1.student_class,student_1.student_id, student_1.parent_id))

#c.execute("SELECT * FROM student")
#print(c.fetchall())

conn.commit()

conn.close()