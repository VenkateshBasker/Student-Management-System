import unittest
import tempfile
from pathlib import Path

from StudentApp.student import Student
from StudentApp.storage import save_students, load_students


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = Path(self.temp_dir.name) / "test_students.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_and_load_students(self):
        student = Student("Arun")
        student.marks = [90, 80, 70, 60, 50]
        student.update_report()

        save_students([student], self.test_file)

        loaded_students = load_students(self.test_file)

        self.assertEqual(len(loaded_students), 1)
        self.assertEqual(loaded_students[0].name, "Arun")
        self.assertEqual(
            loaded_students[0].marks,
            [90, 80, 70, 60, 50]
        )

    def test_load_missing_file(self):
        loaded_students = load_students(self.test_file)

        self.assertEqual(loaded_students, [])

    def test_load_invalid_json(self):
        self.test_file.write_text(
            "{invalid json",
            encoding="utf-8"
        )

        loaded_students = load_students(self.test_file)

        self.assertEqual(loaded_students, [])

    def test_load_empty_list(self):
        self.test_file.write_text(
            "[]",
            encoding="utf-8"
        )

        loaded_students = load_students(self.test_file)

        self.assertEqual(loaded_students, [])


if __name__ == "__main__":
    unittest.main()