# students_mgmt.py
import csv
import os
from datetime import datetime
from config import (
    STUDENTS_CSV,
    STUDENTS_FIELDS,
    VALID_CLASSES,
    VALID_GENDERS,
    VALID_DISABILITY_STATUS,
    VALID_ENTRY_TYPES
)
from utils.utils import clear_screen, input_choice, input_number

# ------------------- CSV Utilities -------------------
def read_csv(file=STUDENTS_CSV):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return list(csv.DictReader(f))

def write_csv(rows, file=STUDENTS_CSV):
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=STUDENTS_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

def get_unique_id(existing_ids, prompt="Enter Student ID: ", current_id=None):
    """Ensure Student ID is unique"""
    while True:
        uid = input(prompt).strip().upper()
        if uid == "" and current_id:
            return current_id
        if uid not in existing_ids:
            return uid
        print("⚠️ This ID already exists! Try another one.")

# ------------------- CRUD Operations -------------------
def adding_students(count=1):
    clear_screen()
    existing_ids = {s["Unique_ID"] for s in read_csv()}
    new_students = []

    for i in range(count):
        print(f"\n--- Adding Student {i + 1} ---")
        unique_id = get_unique_id(existing_ids)
        name = input("Student Name: ").title()
        age = input_number(f"{name}'s Age: ")
        gender = input_choice("Gender", VALID_GENDERS)
        in_class = input_choice("Class", VALID_CLASSES)
        date_joined = datetime.now().strftime("%x %X")
        disability = input_choice("Disability", VALID_DISABILITY_STATUS)
        orphanhood = input_choice("Orphanhood", ["Yes", "No"])
        entry_type = input_choice("Entry Type", VALID_ENTRY_TYPES)
        village = input("Village: ").title()

        student = {
            "Unique_ID": unique_id,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Class": in_class,
            "Date_OF_Join": date_joined,
            "Disability": disability,
            "Orphanhood": orphanhood,
            "First_Entry_or_repeater": entry_type,
            "Village": village
        }

        new_students.append(student)
        existing_ids.add(unique_id)
        print(f"✅ Student {name} added successfully!")

    all_students = read_csv() + new_students
    write_csv(all_students)
    return new_students

def viewing_students():
    students = sorted(read_csv(), key=lambda s: s["Name"])
    if not students:
        print("⚠️ No students found.")
        return
    print("ID | Name | Age | Gender | Class | Date Joined")
    print("-"*50)
    for s in students:
        print(f"{s['Unique_ID']} | {s['Name']} | {s['Age']} | {s['Gender']} | {s['Class']} | {s['Date_OF_Join']}")

def deleting_student():
    students = read_csv()
    if not students:
        print("⚠️ No students found.")
        return
    uid = input("Student ID to delete: ").strip().upper()
    new_list = [s for s in students if s["Unique_ID"] != uid]
    if len(new_list) == len(students):
        print("⚠️ Student not found.")
        return
    write_csv(new_list)
    print("✅ Student deleted successfully.")

def updating_student():
    students = read_csv()
    if not students:
        print("⚠️ No students found.")
        return
    uid = input("Student ID to update: ").strip().upper()
    for idx, s in enumerate(students):
        if s["Unique_ID"] == uid:
            current = s
            break
    else:
        print("⚠️ Student not found.")
        return

    existing_ids = {s["Unique_ID"] for s in students if s["Unique_ID"] != uid}
    print("--- Press Enter to keep current value ---")

    new_id = get_unique_id(existing_ids, current_id=current["Unique_ID"])
    name = input(f"Name [{current['Name']}]: ").title() or current["Name"]
    age = input_number(f"Age [{current['Age']}]: ", allow_empty=True, default=current["Age"])
    gender = input_choice(f"Gender [{current['Gender']}]", VALID_GENDERS, allow_empty=True, default=current["Gender"])
    in_class = input_choice(f"Class [{current['Class']}]", VALID_CLASSES, allow_empty=True, default=current["Class"])
    village = input(f"Village [{current['Village']}]: ").title() or current["Village"]
    disability = input_choice(f"Disability [{current['Disability']}]", VALID_DISABILITY_STATUS, allow_empty=True, default=current["Disability"])
    orphanhood = input_choice(f"Orphanhood [{current['Orphanhood']}]", ["Yes", "No"], allow_empty=True, default=current["Orphanhood"])
    entry_type = input_choice(f"Entry Type [{current['First_Entry_or_repeater']}]", VALID_ENTRY_TYPES, allow_empty=True, default=current["First_Entry_or_repeater"])

    updated_student = {
        "Unique_ID": new_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Class": in_class,
        "Date_OF_Join": datetime.now().strftime("%x %X"),
        "Disability": disability,
        "Orphanhood": orphanhood,
        "First_Entry_or_repeater": entry_type,
        "Village": village
    }

    students[idx] = updated_student
    write_csv(students)
    print("✅ Student updated successfully.")

def search_student():
    students = read_csv()
    if not students:
        print("⚠️ No students found.")
        return
    uid = input("Student ID to search: ").strip().upper()
    for s in students:
        if s["Unique_ID"] == uid:
            print("ID | Name | Age | Gender | Class | Date Joined")
            print(f"{s['Unique_ID']} | {s['Name']} | {s['Age']} | {s['Gender']} | {s['Class']} | {s['Date_OF_Join']}")
            return
    print("⚠️ Student not found.")