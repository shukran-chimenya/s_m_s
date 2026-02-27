# auth.py
"""
Authentication module for School Management System
- Login
- User registration (Admin only)
- Teacher & Admin dashboards
"""

import getpass
import os
import csv
from config import USERS_FILE, VALID_ROLES
from utils.utils import clear_screen, system_header
from students.students import students_mgmt
from students.students_performance_mgmt import students_performance_mgmt
from teachers.teacher_performance_mgmt import generate_teacher_performance
from teachers import teachers_mgmt
from school_dashboard.school_dashboard import (
    generate_school_dashboard,
    generate_term_trend_analysis,
    rank_students_per_class
)

# -------------------- Authentication -------------------- #
def login():
    """Authenticate user and return their role."""
    attempts = 3

    while attempts > 0:
        clear_screen()
        system_header("=== LOGIN ===\n")

        username = input("Username: ").strip()
        password = getpass.getpass("Password: ").strip()

        if not os.path.exists(USERS_FILE):
            print("⚠️ No users registered. Contact admin.")
            input("Press Enter to continue...")
            return None

        with open(USERS_FILE) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Username"] == username and row["Password"] == password:
                    print(f"\n✅ Login successful ({row['Role']})")
                    input("Press Enter to continue...")
                    return row["Role"].lower()

        attempts -= 1
        print(f"\n❌ Invalid credentials. Attempts remaining: {attempts}")

        if attempts == 0:
            print("⚠️ Too many failed login attempts.")
            input("Press Enter to return to main menu...")
            return None

        input("Press Enter to try again...")

def register_user():
    """Register a new user (Admin only)."""
    clear_screen()
    system_header("=== REGISTER NEW USER ===")
    

    username = input("New Username: ").strip()
    password = getpass.getpass("New Password: ").strip()

    while True:
        role = input(f"Role ({'/'.join(VALID_ROLES)}): ").strip().lower()
        if role in VALID_ROLES:
            break
        print(f"⚠️ Invalid role. Choose from: {', '.join(VALID_ROLES)}")

    file_exists = os.path.exists(USERS_FILE)
    with open(USERS_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Username", "Password", "Role"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"Username": username, "Password": password, "Role": role})

    print("\n✅ User registered successfully!")
    input("Press Enter to continue...")


# -------------------- Teacher Dashboard -------------------- #
def teacher_menu():
    """Dashboard accessible to teachers."""
    while True:
        clear_screen()
        system_header("=== TEACHER DASHBOARD ===")
        print("1. Student Management")
        print("2. Student Performance Register")
        print("3. Performance Analysis")
        print("4. End of Term Results")
        print("0. Logout")
        print("-" * 50)

        choice = input("\nSelect option: ").strip()
        if choice == "1":
            students_mgmt()
        elif choice == "2":
            students_performance_mgmt()
        elif choice == "3":
            generate_term_trend_analysis()
        elif choice == "4":
            rank_students_per_class()
        elif choice == "0":
            break
        else:
            print("⚠️ Invalid choice.")
        input("Press Enter to continue...")


# -------------------- Admin Dashboard -------------------- #
def admin_menu():
    """Dashboard accessible to admins/headteachers."""
    while True:
        clear_screen()
        system_header("=== ADMIN DASHBOARD ===")
        print("1. Student Management")
        print("2. Student Performance Register")
        print("3. Performance Analysis")
        print("4. End of Term Results")
        print("5. School Summary Dashboard")
        print("6. Register New User")
        print("7. Teacher Performance Management")
        print("8. Teachers Management")
        print("0. Logout")
        print("-" * 50)

        choice = input("\nSelect option: ").strip()
        if choice == "1":
            students_mgmt()
        elif choice == "2":
            students_performance_mgmt()
        elif choice == "3":
            generate_term_trend_analysis()
        elif choice == "4":
            rank_students_per_class()
        elif choice == "5":
            generate_school_dashboard()
        elif choice == "6":
            register_user()
        elif choice == "7":
            generate_teacher_performance()
        elif choice == "8":
            teachers_mgmt()
        elif choice == "0":
            break
        else:
            print("⚠️ Invalid choice.")
        input("Press Enter to continue...")