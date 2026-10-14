
import unittest
from unittest.mock import patch
from StudentApp.manager import students, add_student, search_student , remove_student , update_student , Student
from contextlib import redirect_stdout
from io import StringIO


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        students.clear()

    def test_add_student(self):
        with patch("builtins.input", side_effect=[
            "Arun",
            "90",
            "85",
            "95",
            "80",
            "75"
        ]):
            add_student()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Arun")
        self.assertEqual(students[0].marks, [90, 85, 95, 80, 75])

    def test_search_student(self):
        with patch("builtins.input", side_effect=[
            "gowtham", "98", "88", "92", "81", "78"
        ]):
            add_student()

        output = StringIO()

        with patch("builtins.input", return_value="gowtham"):
            with redirect_stdout(output):
                search_student()

        self.assertIn("gowtham", output.getvalue())

    def test_remove_student(self):
        self.student = Student("Gowtham")
        students.append(self.student)

        with patch("builtins.input", return_value="Gowtham"):
            remove_student()

        self.assertEqual(len(students), 0)

    def test_remove_nonexistent_student(self):
        self.student = Student("Gowtham")
        students.append(self.student)

        with patch("builtins.input", return_value="Arun"):
            remove_student()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Gowtham")

    def test_update_student_name(self):
        self.student = Student("Gowtham")
        students.append(self.student)

        with patch("builtins.input", side_effect=[
            "1",
            "Gowtham",
            "Arun"
        ]):
            update_student()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Arun")

    def test_update_student_mark(self):
        self.student = Student("Gowtham")
        self.student.marks = [70, 70, 70, 70, 70]
        self.student.update_report()
        students.append(self.student)

        with patch("builtins.input", side_effect=[
            "2",
            "Gowtham",
            "1",
            "95"
        ]):
            update_student()

        self.assertEqual(self.student.marks[0], 95)
        self.assertEqual(self.student.total_marks, 375)
        self.assertEqual(self.student.average_marks, 75)

if __name__ == "__main__":
    unittest.main()