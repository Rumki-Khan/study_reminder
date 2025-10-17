# Study Reminders

Automated Python package to send personalized study reminders to students based on their course and preferred time.

---

## Features

- Manage student data using a JSON file
- Generate personalized study reminders
- Simulate sending reminders via console output
- Log reminders with timestamps to a text file
- Schedule daily reminders using the `schedule` library

---
## Modules

- `students.py`: Basic student list management
- `reminder_generator.py`: Generates customized reminders
- `reminder_sender.py`: Simulates sending via console
- `logger.py`: Logs reminders with timestamps
- `students_manager.py`: Advanced student management (JSON)
- `scheduler.py`: Schedules reminders per user preferences

## Testing

Run unit tests:
```bash
python test.py
```

##  Installation

### 1. Clone the repository

bash
git clone https://github.com/yourusername/study_reminders.git
cd study_reminders

----


### 2. Using Anaconda
pip install schedule


### 3. Install package locally
pip install -e .


-----

## Project Structure

study_reminders/
├── students.py
├── reminder_generator.py
├── reminder_sender.py
├── logger.py
├── students_manager.py
├── scheduler.py
main.py
setup.py
README.md
students.json

## Customization

Edit `students.json` to manage student data.

## Requirements

- Python 3.7+
- schedule

Install dependencies:
```bash
pip install schedule
```


