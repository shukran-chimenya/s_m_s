# config.py

# ---------- CSV Files ----------
STUDENTS_CSV = "data/students.csv"
TEACHERS_CSV = "data/teachers.csv"
PERFORMANCE_CSV = "data/students_performance.csv"
USERS_FILE = "data/users.csv"

# ---------- Students ----------
STUDENTS_FIELDS = [
    "Unique_ID", "Name", "Age", "Gender",
    "Class", "Date_OF_Join", "Disability",
    "Orphanhood", "First_Entry_or_repeater", "Village"
]
# ----------------- USER ROLES -----------------
VALID_ROLES = ["admin", "teacher"]

# Valid terms
VALID_TERMS = ["Term 1", "Term 2", "Term 3"]
# Validation lists
VALID_CLASSES = [
    "Standard 1", "Standard 2", "Standard 3", "Standard 4",
    "Standard 5", "Standard 6", "Standard 7", "Standard 8"
]

VALID_GENDERS = ["Male", "Female"]
VALID_DISABILITY_STATUS = ["Y", "N"]
VALID_ENTRY_TYPES = ["First Entry", "Repeater"]
VALID_ASSESSMENT = ["Bi-weekly", "End-of-Term"]

# ---------- Teachers ----------
TEACHERS_FIELDS = [
    "Emp_ID", "Name", "Age", "Gender",
    "Class_Assigned", "Date_OF_Join",
    "# of Students in Class", "Program"
]

# ---------- Subjects offered in this school ----------
SUBJECTS = [
    "English", "Agriculture", "Mathematics", "Chichewa",
    "Science and Technology", "Social Studies", "Religious Knowledge"
]