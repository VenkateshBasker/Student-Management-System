from StudentApp.manager import (
    students,
    add_student,
    remove_student,
    update_student,
    all_students,
    search_student,
    remove_all,
    save_all
)
from StudentApp.storage import load_students
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    students.extend(load_students())

    while True:
        print("======= STUDENTS MANAGEMENT SYSTEM ======", "\n")
        print(
            " 1.Show all Students", "\n",
            "2.Search Student", "\n",
            "3.Add Student", "\n",
            "4.Remove Student", "\n",
            "5.Update Student", "\n",
            "6.Remove All Students", "\n",
            "7.exit", "\n"
        )
        while True:
            try:
                choice = int(input("Enter Your Choice : "))
                if choice > 7 or choice < 1:
                    print("Invalid Choice")
                else:
                    break
            except ValueError:
                print("Enter a Valid Choice")
        if choice == 1:
            all_students()
        elif choice == 2:
            search_student()
        elif choice == 3:
            add_student()
            save_all()
        elif choice == 4:
            remove_student()
            save_all()
        elif choice == 5:
            update_student()
            save_all()
        elif choice == 6:
            remove_all()
        elif choice == 7:
            save_all()
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()