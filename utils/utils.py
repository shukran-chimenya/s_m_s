# utils.py
"""
Utility functions for School Management System
Includes:
- Screen clearing
- Input validation
- ID uniqueness checks
- Student retrieval by class
"""

import os
import csv
from config import STUDENTS_CSV, STUDENTS_FIELDS, VALID_CLASSES

# ------------------ Screen ------------------ #
def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


# ------------------ Input Validators ------------------ #
def input_number(prompt, min_val=None, max_val=None, allow_empty=False, default=None):
    """
    Safely input an integer, optionally within a range.
    """
    while True:
        val = input(prompt).strip()
        if allow_empty and val == "":
            return default
        try:
            n = int(val)
            if (min_val is not None and n < min_val) or (max_val is not None and n > max_val):
                print(f"⚠️ Enter a number between {min_val} and {max_val}")
                continue
            return n
        except ValueError:
            print("⚠️ Please enter a valid integer!")


def input_choice(prompt, choices, allow_empty=False, default=None, case_sensitive=False):
    """
    Input limited to allowed choices.
    """
    choices_str = "/".join(choices)
    normalized_choices = choices if case_sensitive else [c.lower() for c in choices]

    while True:
        val = input(f"{prompt} ({choices_str}): ").strip()
        if allow_empty and val == "":
            return default
        compare_val = val if case_sensitive else val.lower()
        if compare_val in normalized_choices:
            return choices[normalized_choices.index(compare_val)]
        print(f"⚠️ Enter a valid option: {choices_str}")


def get_unique_id(existing_ids, prompt="Enter ID: ", current_id=None):
    """
    Ensure ID is unique among existing IDs.
    """
    while True:
        uid = input(prompt).strip().upper()
        if uid == "" and current_id:
            return current_id
        if uid not in existing_ids:
            return uid
        print("⚠️ This ID already exists! Try another one.")


# ------------------ Student Utilities ------------------ #
def read_csv(file=STUDENTS_CSV, fields=None):
    """Read CSV file and return list of dicts"""
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return list(csv.DictReader(f, fieldnames=fields))


def get_students_in_class(class_name):
    """
    Return all students in a specific class.
    """
    students = read_csv(STUDENTS_CSV, STUDENTS_FIELDS)
    return [s for s in students if s["Class"] == class_name]


def get_student_by_id(student_id):
    """
    Retrieve a student record by Unique_ID.
    """
    students = read_csv(STUDENTS_CSV, STUDENTS_FIELDS)
    for s in students:
        if s["Unique_ID"].upper() == student_id.upper():
            return s
    return None

def system_header(title):
    clear_screen()
    print("=" * 45)
    print("   SCHOOL MANAGEMENT SYSTEM  ")
    print("=" * 45)
    print(f"{title}")
    print("=" * 50)