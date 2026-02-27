# teachers.py
import csv
import os
from datetime import datetime
from config import TEACHERS_CSV, TEACHERS_FIELDS, VALID_CLASSES, VALID_GENDERS
from utils.utils import clear_screen, input_number, input_choice, get_unique_id

# ------------------- CSV Utilities -------------------
def read_teachers():
    if not os.path.exists(TEACHERS_CSV):
        return []
    with open(TEACHERS_CSV) as f:
        return list(csv.DictReader(f))

def write_teachers(rows):
    with open(TEACHERS_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TEACHERS_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

def get_teacher_by_id(emp_id):
    for t in read_teachers():
        if t["Emp_ID"].upper() == emp_id.upper():
            return t
    return None

# ------------------- Core Functions -------------------
def adding_teachers(count=1):
    clear_screen()
    existing_ids = {t["Emp_ID"] for t in read_teachers()}
    new_teachers = []

    for i in range(count):
        print(f"\n--- Adding Teacher {i+1} ---")
        emp_id = get_unique_id(existing_ids, prompt="Enter Employee ID: ")
        name = input("Teacher Name: ").title()
        age = input_number(f"{name}'s Age: ")
        gender = input_choice(f"Gender for {name}", VALID_GENDERS).title()
        class_assigned = input_choice(f"Class Assigned for {name}", VALID_CLASSES).title()
        date_joined = datetime.now().strftime("%x %X")
        num_students = input_number(f"Number of students in {class_assigned}: ")
        program = input("Program (IPTE): ").title()

        teacher = {
            "Emp_ID": emp_id,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Class_Assigned": class_assigned,
            "Date_OF_Join": date_joined,
            "# of Students in Class": num_students,
            "Program": program
        }

        new_teachers.append(teacher)
        existing_ids.add(emp_id)
        print(f"✅ Teacher {name} added successfully!\n")

    all_teachers = read_teachers() + new_teachers
    write_teachers(all_teachers)
    return new_teachers

def viewing_teachers():
    clear_screen()
    teachers = sorted(read_teachers(), key=lambda t: t["Name"])
    if not teachers:
        print("⚠️ No teachers found.")
        return

    print("Emp_ID | Name | Age | Gender | Class Assigned | Date Joined | # Students | Program")
    print("-"*90)
    for t in teachers:
        print(f"{t['Emp_ID']} | {t['Name']} | {t['Age']} | {t['Gender']} | "
              f"{t['Class_Assigned']} | {t['Date_OF_Join']} | {t['# of Students in Class']} | {t['Program']}")

def deleting_teacher():
    clear_screen()
    teachers = read_teachers()
    if not teachers:
        print("⚠️ No teachers found.")
        return

    emp_id = input("Enter Teacher Employee ID to delete: ").strip().upper()
    new_list = [t for t in teachers if t["Emp_ID"].upper() != emp_id]
    if len(new_list) == len(teachers):
        print("⚠️ Teacher not found.")
        return

    write_teachers(new_list)
    print(f"✅ Teacher {emp_id} deleted successfully.")

def updating_teacher():
    clear_screen()
    teachers = read_teachers()
    if not teachers:
        print("⚠️ No teachers found.")
        return

    emp_id = input("Enter Teacher Employee ID to update: ").strip().upper()
    for idx, t in enumerate(teachers):
        if t["Emp_ID"].upper() == emp_id:
            current = t
            break
    else:
        print("⚠️ Teacher not found.")
        return

    existing_ids = {t["Emp_ID"] for t in teachers if t["Emp_ID"].upper() != emp_id}
    print("--- Press Enter to keep current value ---")

    new_id = get_unique_id(existing_ids, prompt="New Employee ID: ", current_id=current["Emp_ID"])
    name = input(f"Name [{current['Name']}]: ").title() or current["Name"]
    age = input_number(f"Age [{current['Age']}]: ", allow_empty=True, default=current["Age"])
    gender = input_choice(f"Gender [{current['Gender']}]: ", VALID_GENDERS, allow_empty=True, default=current["Gender"]).title()
    class_assigned = input_choice(f"Class Assigned [{current['Class_Assigned']}]: ", VALID_CLASSES, allow_empty=True, default=current["Class_Assigned"]).title()
    num_students = input_number(f"# Students [{current['# of Students in Class']}]: ", allow_empty=True, default=current["# of Students in Class"])
    program = input(f"Program [{current['Program']}]: ").title() or current["Program"]

    updated_teacher = {
        "Emp_ID": new_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Class_Assigned": class_assigned,
        "Date_OF_Join": datetime.now().strftime("%x %X"),
        "# of Students in Class": num_students,
        "Program": program
    }

    teachers[idx] = updated_teacher
    write_teachers(teachers)
    print(f"✅ Teacher {name} updated successfully.")

def search_teacher():
    clear_screen()
    teachers = read_teachers()
    if not teachers:
        print("⚠️ No teachers found.")
        return

    emp_id = input("Enter Teacher Employee ID to search: ").strip().upper()
    teacher = get_teacher_by_id(emp_id)
    if teacher:
        print("Emp_ID | Name | Age | Gender | Class Assigned | Date Joined | # Students | Program")
        print("-"*90)
        print(f"{teacher['Emp_ID']} | {teacher['Name']} | {teacher['Age']} | {teacher['Gender']} | "
              f"{teacher['Class_Assigned']} | {teacher['Date_OF_Join']} | {teacher['# of Students in Class']} | {teacher['Program']}")
    else:
        print("⚠️ Teacher not found.")