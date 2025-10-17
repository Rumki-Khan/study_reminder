# setup.py

from setuptools import setup, find_packages

setup(
    name="study_reminders",
    version="1.0.0",
    author="Rumman Chowdhury",
    author_email="rummansust006@gmail.com",
    description="Automated Python package to send personalized study reminders to students.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "schedule>=1.2.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Topic :: Education :: Testing and Reminder Systems"
    ],
    python_requires=">=3.8",
)
