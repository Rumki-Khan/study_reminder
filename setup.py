# setup.py

from setuptools import setup, find_packages

setup(
    name='study_reminders',
    version='0.1.0',
    description='Automated personalized study reminders',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'schedule>=1.1.0'
    ],
    entry_points={
        'console_scripts': [
            'study-reminders=main:run_now'
        ]
    }
)

