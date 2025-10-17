import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from study_reminders.students import Students





import unittest

class TestStudents(unittest.TestCase):
    def setUp(self):
        self.manager = Students()

    def test_add_student(self):
        self.manager.add_student("Alice", "alice@example.com", "Python", "08:00")
        self.assertEqual(len(self.manager.get_students()), 1)

    def test_remove_student(self):
        self.manager.add_student("Bob", "bob@example.com", "Math", "09:00")
        self.manager.remove_student("Bob")
        self.assertEqual(len(self.manager.get_students()), 0)

    def test_get_students(self):
        self.manager.add_student("Charlie", "charlie@example.com", "Physics", "07:30")
        students = self.manager.get_students()
        print("Students:", students)  # Debug print
        self.assertEqual(students[0]['name'], "Charlie")
        


