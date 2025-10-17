import unittest
from study_reminders.reminder_generator import generate_reminder

class TestReminderGenerator(unittest.TestCase):
    def test_generate_reminder(self):
        result = generate_reminder("Alice", "Python")
        self.assertIn("Hi Alice", result)
        self.assertIn("review Python", result)

