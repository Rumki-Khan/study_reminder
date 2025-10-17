import unittest
import os
import json
from study_reminders.students_manager import StudentsManager

class TestStudentsManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_students.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.manager = StudentsManager(file_path=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_and_get_student(self):
        self.manager.add_student("Dana", "dana@example.com", "AI", "10:00")
        students = self.manager.get_students()
        self.assertEqual(students[0]['name'], "Dana")

    def test_remove_student(self):
        self.manager.add_student("Eli", "eli@example.com", "ML", "11:00")
        self.manager.remove_student("Eli")
        students = self.manager.get_students()
        self.assertEqual(len(students), 0)

    def test_save_and_load_students(self):
        self.manager.add_student("Fay", "fay@example.com", "Data Science", "12:00")
        new_manager = StudentsManager(file_path=self.test_file)
        students = new_manager.get_students()
        self.assertEqual(students[0]['name'], "Fay")
