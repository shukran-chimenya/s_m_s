# main.py
from auth import login, admin_menu, teacher_menu
from utils.utils import clear_screen, system_header


def main():
    """Main entry point of the system."""
    while True:
        clear_screen()
        system_header("\t MAIN MENU ")
        print("1. Login")
        print("0. Exit System")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            role = login()

            if role == "admin":
                admin_menu()

            elif role == "teacher":
                teacher_menu()

            else:
                print("⚠️ Login failed.")
                input("Press Enter to continue...")

        elif choice == "0":
            print("\n👋 Exiting system. Goodbye!")
            break

        else:
            print("⚠️ Invalid selection.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()