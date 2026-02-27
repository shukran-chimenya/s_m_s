# teacher_performance_mgmt.py
"""
Teacher Performance Management

Generates teacher performance reports based on student scores.
Saves evaluations to a CSV file.
"""

import csv
import os
from utils.utils import get_students_in_class, clear_screen
from config import SUBJECTS, TEACHERS_CSV, PERFORMANCE_CSV

TEACHER_PERFORMANCE_FILE = "teachers_performance.csv"
TEACHER_PERFORMANCE_FIELDS = [
    "Emp_ID",
    "Teacher_Name",
    "Class",
    "Term",
    "Class_Average",
    "Score",
    "Status"
]

# ---------------- CSV Utilities ----------------
def read_teacher_performance():
    if not os.path.exists(TEACHER_PERFORMANCE_FILE):
        return []
    with open(TEACHER_PERFORMANCE_FILE) as f:
        return list(csv.DictReader(f))

def write_teacher_performance(rows):
    with open(TEACHER_PERFORMANCE_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TEACHER_PERFORMANCE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

# ---------------- Helper Functions ----------------
def get_teacher_by_id(emp_id):
    """Return teacher row dict for a given Emp_ID"""
    if not os.path.exists(TEACHERS_CSV):
        return None
    with open(TEACHERS_CSV) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Emp_ID"].upper() == emp_id.upper():
                return row
    return None

def get_student_final_scores(student_id, term_selected):
    """Return final scores for a student for a given term"""
    if not os.path.exists(PERFORMANCE_CSV):
        return None

    records = []
    with open(PERFORMANCE_CSV) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Unique_ID"].upper() == student_id.upper() and row["Term"] == term_selected:
                records.append(row)

    if not records:
        return None

    # Prefer end-of-term over bi-weekly averages
    end_term = [r for r in records if r["Assessment_Type"].lower() == "end-of-term"]

    final_scores = {}
    if end_term:
        latest = end_term[-1]
        for subj in SUBJECTS:
            final_scores[subj] = int(latest.get(subj, 0))
    else:
        bi_weekly = [r for r in records if r["Assessment_Type"].lower() == "bi-weekly"]
        for subj in SUBJECTS:
            total = sum(int(r.get(subj, 0)) for r in bi_weekly)
            final_scores[subj] = total // len(bi_weekly) if bi_weekly else 0

    return final_scores

def teacher_grade(class_average):
    """Return performance score and status based on class average"""
    if class_average >= 80:
        return 5, "Outstanding"
    elif class_average >= 70:
        return 4, "Exceeds Expectation"
    elif class_average >= 60:
        return 3, "Meets Expectation"
    elif class_average >= 50:
        return 2, "Needs Improvement"
    else:
        return 1, "Unsatisfactory"

# ---------------- Core Function ----------------
def generate_teacher_performance():
    """Generate teacher performance report based on student averages"""
    clear_screen()
    print("=== Generate Teacher Performance Report ===\n")

    teacher_id = input("Enter Teacher ID: ").strip().upper()
    teacher = get_teacher_by_id(teacher_id)

    if not teacher:
        print("⚠️ Teacher not found.")
        input("Press Enter to return...")
        return

    teacher_name = teacher["Name"]
    assigned_class = teacher["Class_Assigned"]

    # Term selection
    term_selected = _select_term()

    # Prevent duplicate evaluation
    existing_records = read_teacher_performance()
    for record in existing_records:
        if record["Emp_ID"].upper() == teacher_id.upper() and record["Term"] == term_selected:
            print("⚠️ Teacher already evaluated for this term.")
            input("Press Enter to return...")
            return

    # Get students in class
    students = get_students_in_class(assigned_class)
    if not students:
        print("⚠️ No students found in this class.")
        input("Press Enter to return...")
        return

    class_totals = []
    valid_students = 0

    for student in students:
        student_id = student["Unique_ID"]
        final_scores = get_student_final_scores(student_id, term_selected)
        if final_scores:
            student_avg = sum(final_scores.values()) / len(SUBJECTS)
            class_totals.append(student_avg)
            valid_students += 1

    if valid_students == 0:
        print("⚠️ No performance data available for this term.")
        input("Press Enter to return...")
        return

    class_average = round(sum(class_totals) / valid_students, 2)
    score, status = teacher_grade(class_average)

    # Display report
    print("\n--------------------------------------")
    print(f"Teacher: {teacher_name}")
    print(f"Class: {assigned_class}")
    print(f"Term: {term_selected}")
    print(f"Class Average: {class_average}%")
    print(f"Performance Score: {score}")
    print(f"Status: {status}")
    print("--------------------------------------")

    # Save evaluation
    file_exists = os.path.exists(TEACHER_PERFORMANCE_FILE)
    with open(TEACHER_PERFORMANCE_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TEACHER_PERFORMANCE_FIELDS)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "Emp_ID": teacher_id,
            "Teacher_Name": teacher_name,
            "Class": assigned_class,
            "Term": term_selected,
            "Class_Average": class_average,
            "Score": score,
            "Status": status
        })

    print("\n✅ Teacher Performance Saved Successfully")
    input("Press Enter to return...")

# ---------------- Helper ----------------
def _select_term():
    while True:
        term_input = input("Enter Term (1,2,3): ").strip()
        if term_input in ("1", "2", "3"):
            return f"Term {term_input}"
        print("⚠️ Invalid term. Enter 1, 2, or 3.")