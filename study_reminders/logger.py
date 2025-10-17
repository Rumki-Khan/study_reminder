# study_reminders/logger.py

import datetime

def log_reminder(student, reminder):
    """
    Log a sent reminder with a timestamp to a file 'reminder_log.txt'.
    """
    timestamp = datetime.datetime.now().isoformat()
    entry = f"{timestamp} - Sent to {student['name']}: {reminder}\n"
    with open("reminder_log.txt", "a") as log_file:
        log_file.write(entry)
