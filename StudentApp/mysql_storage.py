import mysql.connector
import logging
import os

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.environ["DB_PASSWORD"],
            database=os.getenv("DB_NAME", "student_management")
        )
        return connection

    except (mysql.connector.Error, KeyError):
        logging.exception("Failed to connect to MySQL.")
        raise

def save_students_mysql(students):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        connection.start_transaction()

        current_names = [student.name for student in students]

        cursor.execute("SELECT student_id, name FROM students")
        existing_students = cursor.fetchall()

        for student_id, name in existing_students:
            if name not in current_names:
                cursor.execute(
                    "DELETE FROM student_marks WHERE student_id = %s",
                    (student_id,)
                )
                cursor.execute(
                    "DELETE FROM students WHERE student_id = %s",
                    (student_id,)
                )

        for student in students:
            cursor.execute(
                "SELECT student_id FROM students WHERE name = %s",
                (student.name,)
            )
            result = cursor.fetchone()

            if result:
                student_id = result[0]

                cursor.execute(
                    "DELETE FROM student_marks WHERE student_id = %s",
                    (student_id,)
                )

            else:
                cursor.execute(
                    "INSERT INTO students (name) VALUES (%s)",
                    (student.name,)
                )
                student_id = cursor.lastrowid

            for subject, mark, grade, result in zip(
                    student.subjects,
                    student.marks,
                    student.sub_grades,
                    student.pass_fail
            ):
                cursor.execute(
                    """
                    INSERT INTO student_marks
                        (student_id, subjects, marks, grades, outcome)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (student_id, subject, mark, grade, result)
                )

        connection.commit()
        print("Students saved to MySQL successfully!")

    except Exception:
        if connection is not None and connection.is_connected():
            connection.rollback()

        logging.exception("Failed to save students to MySQL.")
        raise

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()