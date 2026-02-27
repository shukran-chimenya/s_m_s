from students.students_mgmt import adding_students, viewing_students, deleting_student
from students.students_mgmt import updating_student, search_student, clear_screen

def students_mgmt():
    """Student management submenu"""
    while True:
        clear_screen()
        print("*********************************")
        print("*** Student Management ***")
        print("*********************************\n")
        print("\t 1. Add Students")
        print("\t 2. View Students")
        print("\t 3. Delete Students")
        print("\t 4. Update Students")
        print("\t 5. Search Student")
        print("\t 0. Return to Main Menu \n")
        print("*********************************")

        try:
            option = int(input("Select Your Option: "))
        except ValueError:
            print("⚠️ Please enter a number only!")
            input("Press Enter to continue...")
            continue

        match option:
            case 1:
                clear_screen()
                print("**Adding Students**")
                print("----------------------------------------")
                while True:
                    try:
                        number_of_times = int(input("How many students do you want to add: "))
                        adding_students(number_of_times)
                        input("Press Enter to continue...") #To hold the message so that the user can read the message
                        break
                    except ValueError:
                        print("⚠️ Please enter a valid number!")
            case 2:
                clear_screen()
                print("**View All Students**")
                print("----------------------------------------")
                viewing_students()
                input("Press Enter to continue...")
            case 3:
                clear_screen()
                print("**Delete a Student**")
                print("----------------------------------------")
                deleting_student()
                input("Press Enter to continue...")
            case 4:
                clear_screen()
                print("**Update a Student**")
                print("----------------------------------------")
                updating_student()
                input("Press Enter to continue...")
            case 5:
                clear_screen()
                print("**Search for a Student**")
                print("----------------------------------------")
                search_student()
                input("Press Enter to continue...")
            case 0:
                return  # Return to main menu
            case _:
                print("⚠️ Invalid Selection! Try again.")
                input("Press Enter to continue...")
