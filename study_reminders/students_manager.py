# study_reminders/students_manager.py

import json

class StudentsManager:
    """Class to manage student data with JSON storage."""

    def __init__(self, file_path="students.json"):
        self.file_path = file_path
        self.students = []
        self.load_students()

    def load_students(self):
        """Load student data from a JSON file or return defaults."""
        try:
             with open(self.file_path, "r") as f:
                 self.students = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
                self.students = []

    def save_students(self):
        """Save student data to the JSON file."""
        with open(self.file_path, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, name, email, course, preferred_time="08:00 AM"):
        """Add a student and save to the JSON file."""
        student = {
            'name': name,
            'email': email,
            'course': course,
            'preferred_time': preferred_time
        }
        self.students.append(student)
        self.save_students()

    def remove_student(self, name):
        """Remove a student by name and update the JSON file."""
        self.students = [s for s in self.students if s['name'] != name]
        self.save_students()

    def get_students(self):
        """Retrieve the list of students."""
        return self.students

    def list_students(self):
        """Print all students to console."""
        for s in self.students:
            print(f"Name: {s['name']}, Email: {s['email']}, Course: {s['course']}, Preferred Time: {s['preferred_time']}")
