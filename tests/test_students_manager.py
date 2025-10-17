import unittest
import tempfile
import os
import json
from study_reminders.students_manager import StudentsManager

class TestStudentsManager(unittest.TestCase):
    def test_remove_student(self):
    # Start fresh
        self.manager.students = []
        self.manager.save_students()
    
        self.manager.add_student("Eli", "eli@example.com", "ML", "11:00")
        self.manager.remove_student("Eli")
        students = self.manager.get_students()
        self.assertEqual(len(students), 0)

    def setUp(self):
        # Create a temp file path without locking the file
        fd, path = tempfile.mkstemp(suffix=".json")
        os.close(fd)  # Close the file descriptor immediately
        self.temp_file_path = path
        self.manager = StudentsManager(file_path=self.temp_file_path)

    def tearDown(self):
       # Safely delete the temp file
        try:
            os.remove(self.temp_file_path)
        except PermissionError:
            print(f"Could not delete temp file: {self.temp_file_path}")

    def test_add_and_get_student(self):
        self.manager.add_student("Dana", "dana@example.com", "AI", "10:00")
        students = self.manager.get_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Dana")


    def test_save_and_load_students(self):
        self.manager.add_student("Fay", "fay@example.com", "Data Science", "12:00")
        # Reload manager with same temp file
        new_manager = StudentsManager(file_path=self.temp_file_path)
        students = new_manager.get_students()
        self.assertEqual(students[0]['name'], "Fay")


