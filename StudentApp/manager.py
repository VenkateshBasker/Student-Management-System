from .student import Student
import logging
from StudentApp.storage import save_students
from StudentApp.mysql_storage import save_students_mysql

students=[]
key="Venky@979"

def add_student():
    add_students= input("Enter Student Name to Add : ").strip()
    if not add_students:
        print("Student Name Cannot Be Empty")
        return
    for y in students:
        if y.name.lower() == add_students.lower():
            print("Student Already Exists!!!")
            return
    student=Student(add_students)
    student.get_marks()
    student.generate_report()
    students.append(student)
    print("Student Added!")
    logging.info("Student Added Successfully! : %s",student.name)

def remove_student():
    remove_students= input("Enter Student Name to Remove : ")
    found=False
    for r in students:
        if r.name==remove_students:
            students.remove(r)
            found=True
            print("Student Removed!")
            logging.info("Student Removed %s",r.name)
            break
    if not found:
        print("Student Not Found")

def update_student():
    print("1.Update Student's Name")
    print("2.Update Student's Mark")
    print("3.Back","\n")
    while True:
        try:
            choose = int(input("Enter Your Option : "))
            if choose > 3 or choose < 1:
                print("Invalid Choice!!!")
            else:
                break
        except ValueError:
            print("Enter a Valid Number!!!")

    if choose == 1:
        update_name = input("Enter Student Name to Update : ")
        found = False
        for u in students:
            if u.name == update_name:
                new = input("Enter Student's New Name : ")
                u.name = new
                found = True
                print("Student Updated!!!")
                logging.info(
                    "Student name updated from %s to %s",
                    update_name,
                    u.name
                )
                break
        if not found:
            print("Student Not Found")
    if choose == 2:
        student_name = input("Enter Student Name : ")
        found = False
        for m in students:
            if m.name == student_name:
                found = True
                print("===== Choose a Subject to Update =====")
                for i,s in enumerate(m.subjects, start=1):
                    print(f"{i}. {s}")
                while True:
                    try:
                        sub_choose = int(input("Enter Your Option : "))
                        if sub_choose > 5 or sub_choose < 1:
                            print("Invalid Choice!!!")
                        else:
                            break
                    except ValueError:
                        print("Enter a Valid Option!!!")

                index = sub_choose - 1

                while True:
                    try:
                        new_mark = int(input(f"Enter {m.subjects[index]} New Mark : "))
                        if new_mark > 100 or new_mark < 0:
                            print("Enter a Valid Mark")
                        else:
                            m.marks[index] = new_mark
                            m.update_report()
                            print("Student Updated!!!")
                            logging.info(
                                "Updated %s's mark in %s to %s",
                                m.name,
                                m.subjects[index],
                                new_mark
                            )
                            break
                    except ValueError:
                        print("Enter a Valid Mark!!!")
                break

        if not found:
            print("Student Not Found")

    if choose == 3:
        return

def all_students():
    print("========== ALL STUDENTS ==========")
    if len(students) == 0:
        print("No Students")
    else:
        for x,y in zip(students,range(1,len(students)+1)):
            print(f"{y}. {x.name}")

def search_student():
    search_name = input("Enter Student Name to Search : ")
    found=False
    for y in students:
        if y.name == search_name:
            y.display_report()
            found = True
            break

    if not found:
        print("Student Not Found")

def remove_all():
    remove_all=input("Enter Key to Remove All Records : ")
    if remove_all == key:
        students.clear()
        save_students(students)
        save_students_mysql(students)
        print("ALL RECORDS REMOVED!!!")

def save_all():
    save_students(students)
    save_students_mysql(students)
