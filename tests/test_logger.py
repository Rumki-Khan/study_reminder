import unittest
import os
from study_reminders.logger import log_reminder

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.student = {'name': 'Alice'}
        self.reminder = "Review Python"
        self.log_file = "reminder_log.txt"
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_reminder(self):
        log_reminder(self.student, self.reminder)
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, "r") as f:
            content = f.read()
            self.assertIn("Alice", content)
            self.assertIn("Review Python", content)

