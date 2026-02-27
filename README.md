# School Management System (Console-Based) v1.0

A Python-based **School Management System** designed to help schools manage students, teachers, academic performance, and school analytics through a simple console interface.

The system supports **role-based authentication**, allowing **Administrators** and **Teachers** to access different features securely.

---

## 📌 Features

### 🔐 Authentication System
- Secure login system
- Role-based access:
  - **Admin**
  - **Teacher**
- Limited login attempts for security
- Admin can register new users

### 🧑‍🎓 Student Management
- Add new students
- View students
- Update student details
- Delete student records
- Store student information in CSV files

### 🧑‍🏫 Teacher Management
- Register teachers
- Assign teachers to classes
- View teacher information

### 📈 Student Performance Management
- Record student scores per subject
- Store results per term
- Calculate student averages
- Retrieve academic records

### 📊 Performance Analysis
The system automatically generates:
- Term performance trends
- Student ranking per class
- Class performance averages

### 🏫 School Dashboard
Provides a summary of school performance, including:
- Overall school average per term
- Best performing class 🏆
- Worst performing class ⚠
- Best performing teacher 🥇
- Teachers needing improvement 📉

---

## ⚙️ System Requirements
- **Python 3.8 or higher**
- Works on:
  - Windows
  - Linux
  - MacOS
- No external libraries required

---

## 🔑 Login System
Users must log in before accessing the system.

**Example users stored in `users.csv`:**

| Username | Password  | Role    |
|----------|-----------|---------|
| admin    | admin123  | admin   |
| teacher1 | pass123   | teacher |

**Roles available:**
- `admin`
- `teacher`

---

## 🛠 Admin Capabilities
Admins can:
- Manage students
- Register teachers
- Register system users
- Record student performance
- View school dashboard
- View teacher performance
- Rank students
- Analyze term performance

---

## 🛠 Teacher Capabilities
Teachers can:
- Manage students
- Record student performance
- View class results
- View term analysis
- Rank students in their class

---

## 🔄 Example System Flow
```text
Start System
      │
      ▼
   Login Screen
      │
      ▼
   Role Detected
 ┌───────┴────────┐
 ▼                ▼
Admin Menu      Teacher Menu
💾 Data Storage

The system stores data using CSV files:

File               	Purpose
students.csv	Stores student information
teachers.csv	Stores teacher details
users.csv	     Stores login credentials
performance.csv	Stores student scores


🔒 Security Features

Login attempt limit

Role-based access control

Restricted admin features

📂 Project Folder Structure
school_management_system/
│
├── main.py
├── config.py
├── auth.py
├── students/
│   ├── students_mgmt.py
│   └── students_performance_mgmt.py
├── teachers/
│   ├── teachers_mgmt.py
│   └── teachers_performance_mgmt.py
├── dashboard/
│   └── school_dashboard.py
├── utils/
│   └── utils.py
├── data/
│   ├── students.csv
│   ├── teachers.csv
│   ├── users.csv
│   └── performance.csv
└── README.md


🚀 Future Improvements

Database integration (SQLite)
GUI version (Tkinter)
Automatic report card generation
Graph-based analytics
Web-based system (Flask)

👤 Author
Shukran Chimenya
I developed this system as a learning project to demonstrate:
File handling
Modular programming
Role-based systems
Data analysis in Python

📄 License

This project is open-source and free to use for educational purposes.

System Status: Stable and fully functional ⚖️

