import json
import os
import tempfile
from .student import Student
from pathlib import Path
import logging

JSON_FILE = Path(__file__).resolve().parent.parent / "students.json"

def save_students(students,path=None):
    destination = Path(path) if path is not None else JSON_FILE
    student_data = []

    for student in students:
        student_data.append({
            "name": student.name,
            "marks": student.marks,
            "subjects": student.subjects
        })

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir = destination.parent,
            delete=False
        ) as file:
            temp_path = Path(file.name)
            json.dump(student_data, file, indent=4)
            file.flush()
            os.fsync(file.fileno())

        os.replace(temp_path, destination)
        print("Students saved successfully!")
        logging.info("Student records saved successfully.")

    except (OSError, TypeError, ValueError):
        logging.exception("Failed to save student records.")
        print("Could not save student records.")

        if temp_path is not None:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                logging.warning("Could not remove the temporary file.")

def load_students(path=None):
    source = Path(path) if path is not None else JSON_FILE
    loaded_students = []

    try:
        with open(source, "r", encoding="utf-8") as file:
            student_data = json.load(file)

        if not isinstance(student_data, list):
            logging.error("Student data must be a JSON list.")
            print("Invalid student data format.")
            return []

        for data in student_data:
            if not isinstance(data, dict):
                print("Skipping an invalid student record.")
                continue

            if not isinstance(data.get("name"), str) or not data["name"].strip():
                print("Skipping a student with an invalid name.")
                continue

            if not isinstance(data.get("marks"), list):
                print("Skipping a student with invalid marks.")
                continue

            if len(data["marks"]) != 5 or not all(
                    type(mark) is int and 0 <= mark <= 100
                    for mark in data["marks"]
            ):
                print("Skipping a student with invalid marks.")
                continue

            student = Student(data["name"])
            student.marks = data["marks"]
            subjects = data.get("subjects", student.subjects)

            if (
                    not isinstance(subjects, list)
                    or len(subjects) != 5
                    or not all(isinstance(subject, str) for subject in subjects)
            ):
                print("Skipping a student with invalid subjects.")
                continue
            student.subjects = subjects
            student.update_report()
            loaded_students.append(student)

        print("Student Record loaded successfully!")

    except FileNotFoundError:
        print("No saved file found. Starting a new record.")
        logging.warning("Student data file was not found.")
        return []
    except json.JSONDecodeError:
        print("The JSON file is empty or invalid. Starting a new record.")
        logging.error("Student data file contains invalid JSON.")
        return []
    return loaded_students