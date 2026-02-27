from teachers_mgmt import adding_teachers, viewing_teachers, deleting_teacher
from teachers_mgmt import updating_teacher, search_teacher
from students.students_mgmt import clear_screen

def teachers_mgmt():
    """Teacher management submenu"""
    while True:
        clear_screen()
        print("*********************************")
        print("*** Teacher Management ***")
        print("*********************************\n")
        print("\t 1. Add Teachers")
        print("\t 2. View Teachers")
        print("\t 3. Delete Teachers")
        print("\t 4. Update Teachers")
        print("\t 5. Search Teacher")
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
                print("**Add Teachers**")
                while True:
                    try:
                        number_of_times = int(input("How many teachers do you want to add: "))
                        adding_teachers(number_of_times)
                        input("Press Enter to continue...")
                        break
                    except ValueError:
                        print("⚠️ Please enter a valid number!")
            case 2:
                clear_screen()
                print("**View All Teachers**")
                print("----------------------------------------")
                viewing_teachers()
                input("Press Enter to continue...")
            case 3:
                clear_screen()
                print("**Delete a Teacher**")
                print("----------------------------------------")
                deleting_teacher()
                input("Press Enter to continue...")
            case 4:
                clear_screen()
                print("**Update a Teacher**")
                print("----------------------------------------")
                updating_teacher()
                input("Press Enter to continue...")
            case 5:
                clear_screen()
                print("**Search for a Teacher**")
                print("----------------------------------------")
                search_teacher()
                input("Press Enter to continue...")
            case 0:
                return  # Return to main menu
            case _:
                print("⚠️ Invalid Selection! Try again.")
                input("Press Enter to continue...")
