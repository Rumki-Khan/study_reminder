# study_reminders/reminder_sender.py

def send_reminder(email, reminder):
    """
    Simulate sending a reminder to the specified email.
    Raises ValueError if email is missing.
    """
    if not email:
        raise ValueError("Email address is missing")
    print(f"Sending reminder to {email}: {reminder}")

