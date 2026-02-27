# school_dashboard.py
"""
School Dashboard & Analysis

Provides text-based dashboards:
📊 Overall School Average per Term
🏆 Best/Worst Performing Class
🥇 Best Performing Teacher
📉 Teachers needing intervention
"""

import os
import csv
from utils.utils import get_students_in_class, clear_screen, system_header
from teachers.teacher_performance_mgmt import get_student_final_scores, teacher_grade
from config import SUBJECTS, TEACHERS_CSV

# ------------------------------
# School Summary Dashboard
# ------------------------------
def generate_school_dashboard():
    clear_screen()
    system_header("SCHOOL SUMMARY DASHBOARD")

    term_selected = _select_term()

    if not os.path.exists(TEACHERS_CSV):
        print("⚠️ No teachers file found.")
        return

    class_results = []
    teacher_results = []

    with open(TEACHERS_CSV) as f:
        reader = csv.DictReader(f)
        for teacher in reader:
            teacher_name = teacher["Name"]
            assigned_class = teacher["Class_Assigned"]

            students = get_students_in_class(assigned_class)
            class_totals = []

            for student in students:
                final_scores = get_student_final_scores(student["Unique_ID"], term_selected)
                if final_scores:
                    student_avg = sum(final_scores.values()) / len(SUBJECTS)
                    class_totals.append(student_avg)

            if class_totals:
                class_average = round(sum(class_totals) / len(class_totals), 2)
                score, status = teacher_grade(class_average)
                class_results.append((assigned_class, class_average))
                teacher_results.append((teacher_name, assigned_class, class_average, score, status))

    if not class_results:
        print("⚠️ No academic data found for this term.")
        input("Press Enter to return...")
        return

    # School-level analytics
    school_average = round(sum([c[1] for c in class_results]) / len(class_results), 2)
    best_class = max(class_results, key=lambda x: x[1])
    worst_class = min(class_results, key=lambda x: x[1])
    best_teacher = max(teacher_results, key=lambda x: x[3])
    low_performers = [t for t in teacher_results if t[3] <= 2]

    # Display Dashboard
    print("--------------------------------------")
    print(f"Term: {term_selected}")
    print(f"Overall School Average: {school_average}%")
    print("--------------------------------------")
    print(f"Best Performing Class: {best_class[0]} ({best_class[1]}%)")
    print(f"Worst Performing Class: {worst_class[0]} ({worst_class[1]}%)")
    print("--------------------------------------")
    print(f"Best Teacher: {best_teacher[0]} ({best_teacher[4]})")
    print("--------------------------------------")

    if low_performers:
        print("Teachers Needing Improvement:")
        for t in low_performers:
            print(f"- {t[0]} ({t[4]})")
    else:
        print("No teachers under intervention level 👌")

    print("--------------------------------------")
    input("Press Enter to return...")

# ------------------------------
# Term Trend Analysis
# ------------------------------
def generate_term_trend_analysis():
    clear_screen()
    system_header("=== SCHOOL TERM TREND ANALYSIS ===")

    if not os.path.exists(TEACHERS_CSV):
        print("⚠️ Teachers file not found.")
        input("Press Enter to return...")
        return

    term_averages = {}

    for term_number in ("1", "2", "3"):
        term_selected = f"Term {term_number}"
        class_results = []

        with open(TEACHERS_CSV) as f:
            reader = csv.DictReader(f)
            for teacher in reader:
                assigned_class = teacher["Class_Assigned"]
                students = get_students_in_class(assigned_class)
                class_totals = []

                for student in students:
                    final_scores = get_student_final_scores(student["Unique_ID"], term_selected)
                    if final_scores:
                        student_avg = sum(final_scores.values()) / len(SUBJECTS)
                        class_totals.append(student_avg)

                if class_totals:
                    class_average = sum(class_totals) / len(class_totals)
                    class_results.append(class_average)

        term_averages[term_selected] = round(sum(class_results) / len(class_results), 2) if class_results else 0

    # Display Results
    print("--------------------------------------")
    print("TERM PERFORMANCE SUMMARY")
    print("--------------------------------------")
    for term, avg in term_averages.items():
        print(f"{term}: {avg}%")

    trend = _determine_trend(term_averages)
    print("--------------------------------------")
    print(f"Overall Trend: {trend}")
    print("--------------------------------------")
    input("Press Enter to return...")

# ------------------------------
# Student Ranking per Class
# ------------------------------
def rank_students_per_class():
    clear_screen()
    system_header("=== STUDENT POSITIONS PER CLASS ===")

    term_selected = _select_term()
    selected_class = input("Enter Class (e.g. Standard 4): ").strip().title()
    students = get_students_in_class(selected_class)

    if not students:
        print("⚠️ No students found in this class.")
        input("Press Enter to return...")
        return

    ranking = []
    for student in students:
        final_scores = get_student_final_scores(student["Unique_ID"], term_selected)
        if final_scores:
            avg_score = round(sum(final_scores.values()) / len(SUBJECTS), 2)
            ranking.append((student["Name"], avg_score))

    if not ranking:
        print("⚠️ No performance data available for this class in this term.")
        input("Press Enter to return...")
        return

    # Sort descending
    ranking.sort(key=lambda x: x[1], reverse=True)

    print("--------------------------------------")
    print(f"Ranking: {selected_class} | {term_selected}")
    print("--------------------------------------")

    position = 0
    previous_score = None
    actual_index = 0
    for name, avg in ranking:
        actual_index += 1
        if avg != previous_score:
            position = actual_index
        print(f"{position}. {name:<20} {avg}")
        previous_score = avg

    print("--------------------------------------")
    input("Press Enter to return...")

# ------------------------------
# Helper Functions
# ------------------------------
def _select_term():
    while True:
        term_input = input("Enter Term (1,2,3): ").strip()
        if term_input in ("1", "2", "3"):
            return f"Term {term_input}"
        print("⚠️ Invalid term. Please enter 1, 2, or 3.")

def _determine_trend(term_averages):
    t1, t2, t3 = term_averages["Term 1"], term_averages["Term 2"], term_averages["Term 3"]
    if t3 > t2 > t1:
        return "🏆 Improving Across Terms"
    elif t3 < t2 < t1:
        return "🥉 Declining Performance"
    else:
        return "⚖️ Mixed / Stable Performance"