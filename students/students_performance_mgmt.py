# students_performance_mgmt.py
import csv
import os
from datetime import datetime
from config import STUDENTS_CSV, SUBJECTS, VALID_TERMS, VALID_ASSESSMENT
from utils.utils import clear_screen, input_choice, input_number

PERFORMANCE_FILE = "data/students_performance.csv"
PERFORMANCE_FIELDS = ["Unique_ID", "Name", "Class", "Term", "Date", "Assessment_Type"] + SUBJECTS

# ------------------- CSV Utilities -------------------
def read_students():
    if not os.path.exists(STUDENTS_CSV):
        return []
    with open(STUDENTS_CSV) as f:
        return list(csv.DictReader(f))

def read_performance():
    if not os.path.exists(PERFORMANCE_FILE):
        return []
    with open(PERFORMANCE_FILE) as f:
        return list(csv.DictReader(f))

def write_performance(rows):
    with open(PERFORMANCE_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=PERFORMANCE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

def get_student_by_id(student_id):
    for s in read_students():
        if s["Unique_ID"].upper() == student_id.upper():
            return {"Unique_ID": s["Unique_ID"], "Name": s["Name"], "Class": s["Class"]}
    return None

# ------------------- Core Functions -------------------
def adding_performance():
    clear_screen()
    print("=== Add Student Performance ===")
    student_id = input("Enter Student ID: ").strip().upper()
    student = get_student_by_id(student_id)
    if not student:
        print("⚠️ Student not found.")
        return

    term = input_choice("Enter Term", VALID_TERMS)
    assessment_type = input_choice("Assessment Type", VALID_ASSESSMENT)
    date_now = datetime.now().strftime("%x %X")

    # Prevent duplicate end-of-term entries
    performances = read_performance()
    if assessment_type.lower() == "end-of-term":
        for row in performances:
            if row["Unique_ID"].upper() == student_id and row["Term"] == term and row["Assessment_Type"].lower() == "end-of-term":
                print("❌ End-of-Term record already exists for this student in this term.")
                return

    # Collect subject scores
    scores = {subj: input_number(f"{subj} score: ") for subj in SUBJECTS}

    # Append record
    record = {
        "Unique_ID": student["Unique_ID"],
        "Name": student["Name"],
        "Class": student["Class"],
        "Term": term,
        "Date": date_now,
        "Assessment_Type": assessment_type
    }
    record.update(scores)
    performances.append(record)
    write_performance(performances)
    print(f"✅ Performance for {student['Name']} added successfully!")

def viewing_performances():
    clear_screen()
    print("=== All Student Performances ===")
    performances = read_performance()
    if not performances:
        print("⚠️ No performance records found.")
        return

    for i, p in enumerate(performances, 1):
        print("-"*50)
        print(f"{i}. {p['Name']} ({p['Unique_ID']}) - {p['Class']}")
        print(f"Term: {p['Term']} | Assessment: {p['Assessment_Type']} | Date: {p['Date']}")
        for subj in SUBJECTS:
            print(f"{subj}: {p[subj]}")
    print("-"*50)

def search_performance():
    clear_screen()
    print("=== Search Student Performance ===")
    student_id = input("Enter Student ID: ").strip().upper()
    performances = [p for p in read_performance() if p["Unique_ID"].upper() == student_id]
    if not performances:
        print("⚠️ No performance records found for this student.")
        return

    for p in performances:
        print("-"*50)
        print(f"{p['Name']} ({p['Unique_ID']}) - {p['Class']}")
        print(f"Term: {p['Term']} | Assessment: {p['Assessment_Type']} | Date: {p['Date']}")
        for subj in SUBJECTS:
            print(f"{subj}: {p[subj]}")
    print("-"*50)

def generate_report():
    clear_screen()
    print("=== Generate Student Report ===")
    student_id = input("Enter Student ID: ").strip().upper()
    term = input_choice("Enter Term", VALID_TERMS)
    performances = [p for p in read_performance() if p["Unique_ID"].upper() == student_id and p["Term"] == term]

    if not performances:
        print("⚠️ No performance records found for this student in this term.")
        return

    # Determine which record to use
    end_term = [p for p in performances if p["Assessment_Type"].lower() == "end-of-term"]
    if end_term:
        latest = end_term[-1]
    else:
        bi_weekly = [p for p in performances if p["Assessment_Type"].lower() == "bi-weekly"]
        latest = {subj: sum(int(r[subj]) for r in bi_weekly)//len(bi_weekly) for subj in SUBJECTS}

    # Grading function
    def grade(score):
        if score <= 39: return "Needs Support"
        elif score <= 59: return "Average"
        elif score <= 69: return "Good"
        elif score <= 79: return "Very Good"
        return "Excellent"

    final_scores = {subj: int(latest.get(subj, 0)) for subj in SUBJECTS}
    overall_avg = sum(final_scores.values()) // len(SUBJECTS)
    overall_grade = grade(overall_avg)
    status = "PASS" if overall_avg >= 50 else "FAIL"

    student_info = get_student_by_id(student_id)
    print("-"*50)
    print(f"Student: {student_info['Name']} | Class: {student_info['Class']} | Term: {term}")
    print("-"*50)
    for subj, score in final_scores.items():
        print(f"{subj}: {score} -> {grade(score)}")
    print("-"*50)
    print(f"Overall Average: {overall_avg}")
    print(f"Overall Grade: {overall_grade}")
    print(f"Final Status: {status}")
    print("-"*50)

# ------------------- Student Performance Menu -------------------
def students_performance_mgmt():
    while True:
        clear_screen()
        print("=== Student Performance Management ===")
        print("=" * 50)
        print("1. Add Student Performance")
        print("2. View All Performances")
        print("3. Search Student Performance")
        print("4. Generate Student Report")
        print("0. Return to Main Menu")
        print("=" * 50)
        choice = input("Select Option: ").strip()
        if choice == "1":
            adding_performance()
            input("Press Enter to continue...")
        elif choice == "2":
            viewing_performances()
            input("Press Enter to continue...")
        elif choice == "3":
            search_performance()
            input("Press Enter to continue...")
        elif choice == "4":
            generate_report()
            input("Press Enter to continue...")
        elif choice == "0":
            return
        else:
            print("⚠️ Invalid selection")
            input("Press Enter to try again...")