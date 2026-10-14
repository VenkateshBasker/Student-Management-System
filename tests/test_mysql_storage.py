import os
import unittest
from unittest.mock import MagicMock, patch

from StudentApp.mysql_storage import (
    get_connection,
    save_students_mysql,
)


class TestMySQLStorage(unittest.TestCase):

    @patch("StudentApp.mysql_storage.mysql.connector.connect")
    @patch.dict(os.environ, {"DB_PASSWORD": "test_password"})
    def test_get_connection(self, mock_connect):
        mock_connect.return_value = MagicMock()

        connection = get_connection()

        self.assertIsNotNone(connection)
        mock_connect.assert_called_once()

    @patch("StudentApp.mysql_storage.get_connection")
    def test_save_students_mysql(self, mock_get_connection):
        connection = MagicMock()
        cursor = MagicMock()

        mock_get_connection.return_value = connection
        connection.cursor.return_value = cursor

        # Simulate an empty students table
        cursor.fetchall.return_value = []

        student = MagicMock()
        student.name = "Test Student"
        student.subjects = [
            "Tamil",
            "English",
            "Maths",
            "Science",
            "Social",
        ]
        student.marks = [90, 85, 95, 80, 88]
        student.sub_grades = ["A", "B", "A", "B", "B"]
        student.pass_fail = ["Pass", "Pass", "Pass", "Pass", "Pass"]

        # Simulate a newly inserted student ID
        cursor.lastrowid = 1

        save_students_mysql([student])

        connection.commit.assert_called_once()
        connection.rollback.assert_not_called()
        connection.close.assert_called_once()

    @patch("StudentApp.mysql_storage.get_connection")
    def test_save_rolls_back_on_error(self, mock_get_connection):
        connection = MagicMock()
        cursor = MagicMock()

        mock_get_connection.return_value = connection
        connection.cursor.return_value = cursor

        # Simulate a database error during the first query
        cursor.execute.side_effect = Exception(
            "Simulated database error"
        )

        with self.assertRaises(Exception):
            save_students_mysql([])

        connection.rollback.assert_called_once()
        connection.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()