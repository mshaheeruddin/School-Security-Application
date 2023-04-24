import unittest
import sqlite3
import queue

from database.school_db import getParentName, getStudents, getStudentClass, getStudentName

conn = sqlite3.connect(r'C:\Users\Muhammad Shaheer\Desktop\School-Security-App\database\school.db')
c = conn.cursor()

class TestStudentFunctions(unittest.TestCase):

    def test_get_parent_name(self):
        expected_output = 'John Doe'
        self.assertEqual(getParentName('S001'), expected_output)

    def test_get_students(self):
        expected_output = ['S001', 'S002', 'S003']
        self.assertEqual(getStudents(), expected_output)

    def test_get_student_class(self):
        expected_output = '12B'
        self.assertEqual(getStudentClass('S001'), expected_output)

    def test_get_student_name(self):
        expected_output = 'Jane Doe'
        self.assertEqual(getStudentName('S002'), expected_output)

if __name__ == '__main__':
    unittest.main()