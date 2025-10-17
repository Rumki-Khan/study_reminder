# study_reminders/scheduler.py

import schedule
import time

def schedule_reminders(students_manager, reminder_generator, reminder_sender, logger):
    """
    Schedule reminder delivery for each student at their preferred time.
    This function runs indefinitely.
    """
    def job(student):
        reminder = reminder_generator(student['name'], student['course'])
        reminder_sender(student['email'], reminder)
        logger(student, reminder)

    for student in students_manager.get_students():
        schedule.every().day.at(student['preferred_time']).do(job, student)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute


