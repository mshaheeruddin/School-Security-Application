import sqlite3
import queue

# create a connection to the database
conn = sqlite3.connect(r'C:\Users\Muhammad Shaheer\Desktop\School-Security-App\database\school.db')

# create a cursor object to execute SQL statements
c = conn.cursor()


def getParentName(id):

  #create the student table
      c.execute(f"""
           SELECT parent.parent_name
           FROM student
           INNER JOIN parent ON student.parent_id = parent.id
           WHERE student.student_id = '{id}'
                  """)

   # commit the changes and close the connection
      conn.commit()

    # fetch the result of the query
      result = c.fetchall()
      result = str(result)
      # print the result
      result = result.replace("[('", "")
      result = result.replace("',)]", "")
      return result


#get all students by their id
#insert them into queue

def getStudents():
    # Create an empty queue
    q = queue.Queue()

    # create the student table
    c.execute("""
               SELECT student_id FROM student
               
                      """)

    # commit the changes and close the connection
    conn.commit()

    # fetch the result of the query
    result = c.fetchall()
    result = str(result).replace("(", "")
    result = str(result).replace(",)", "")
    result = str(result).replace("[", "")
    result = str(result).replace("]", "")
    result = str(result).replace("'", "")
    result = str(result).replace(" ", "")
    result = result.split(",")

    return result


def getStudentClass(id):


    # create the student table
    c.execute(f"""
               SELECT student_class FROM student WHERE student_id = {id}

                      """)

    # commit the changes and close the connection
    conn.commit()

    # fetch the result of the query
    result = str(c.fetchone())
    result = str(result).replace("(", "")
    result = str(result).replace(",)", "")
    result = str(result).replace("'", "")
    return result

def getStudentName(id):


    # create the student table
    c.execute(f"""
               SELECT student_name FROM student WHERE student_id = {id}

                      """)

    # commit the changes and close the connection
    conn.commit()

    # fetch the result of the query
    result = str(c.fetchone())
    result = str(result).replace("(", "")
    result = str(result).replace(",)", "")
    result = str(result).replace("'", "")
    return result

# # create the parent table
# c.execute('''CREATE TABLE parent (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 parent_name TEXT NOT NULL,
#                 student_name TEXT NOT NULL,
#                 relationship TEXT NOT NULL,
#                 phone_number TEXT UNIQUE NOT NULL,
#                 vehicle_number TEXT,
#                 vehicle_type TEXT,
#                 FOREIGN KEY (student_name) REFERENCES student (student_name)
#             );''')

#insert into student table
# c.execute("""
# INSERT INTO student (student_name, first_name, last_name, student_class, student_id, parent_id)
# VALUES
#     ('John Smith', 'John', 'Smith', '10th', '1234', 1),
#     ('Mary Johnson', 'Mary', 'Johnson', '11th', '5678', 2),
#     ('Tom Williams', 'Tom', 'Williams', '9th', '9012', 3);
# """)
#
# #insert into parent table
# c.execute("""
# INSERT INTO parent (parent_name, student_name, relationship, phone_number, vehicle_number, vehicle_type)
# VALUES
#     ('Jane Smith', 'John Smith', 'Mother', '123-456-7890', 'ABC123', 'Car'),
#     ('Bob Johnson', 'Mary Johnson', 'Father', '234-567-8901', 'XYZ456', 'Bus'),
#     ('Sarah Williams', 'Tom Williams', 'Guardian', '345-678-9012', NULL, NULL);
# """)



print(getParentName("1234"))
getStudents()