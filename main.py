# main.py

from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder
from study_reminders.scheduler import schedule_reminders

def run_now():
    """
    Manually trigger one round of reminders for testing.
    """
    manager = StudentsManager()
    for student in manager.get_students():
        reminder = generate_reminder(student['name'], student['course'])
        send_reminder(student['email'], reminder)
        log_reminder(student, reminder)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Study Reminders Automation")
    parser.add_argument(
        '--run-once', action='store_true',
        help="Send all reminders immediately and exit."
    )
    args = parser.parse_args()

    if args.run_once:
        run_now()
    else:
        manager = StudentsManager()
        schedule_reminders(manager, generate_reminder, send_reminder, log_reminder)


