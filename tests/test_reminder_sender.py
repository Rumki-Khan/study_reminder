import unittest
from study_reminders.reminder_sender import send_reminder

class TestReminderSender(unittest.TestCase):
    def test_send_reminder_valid(self):
        try:
            send_reminder("alice@example.com", "Reminder text")
        except Exception:
            self.fail("send_reminder raised Exception unexpectedly!")

    def test_send_reminder_missing_email(self):
        with self.assertRaises(ValueError):
            send_reminder("", "Reminder text")


