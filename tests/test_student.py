import unittest
from StudentApp.student import Student
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Arun")
        self.student.marks = [99,99,99,99,99]
        self.student.calculate_marks()

    def test_grade_a(self):
        self.assertEqual(self.student.total_marks, 495)
        self.assertEqual(self.student.average_marks, 99)
        self.assertEqual(self.student.calculate_grades(), "Grade A")

    def test_grade_b(self):
        self.student.total_marks = 420
        self.assertEqual(self.student.calculate_grades(), "Grade B")

    def test_grade_c(self):
        self.student.total_marks = 375
        self.assertEqual(self.student.calculate_grades(), "Grade C")

    def test_grade_d(self):
        self.student.total_marks = 300
        self.assertEqual(self.student.calculate_grades(), "Grade D")

    def test_grade_e(self):
        self.student.total_marks = 200
        self.assertEqual(self.student.calculate_grades(), "Grade E")

    def test_grade_a_boundary(self):
        self.student.total_marks = 450
        self.assertEqual(self.student.calculate_grades(), "Grade A")

        self.student.total_marks = 449
        self.assertEqual(self.student.calculate_grades(), "Grade B")

if __name__ == "__main__":
    unittest.main()