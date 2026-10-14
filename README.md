# Student Management System

A Python-based Student Management System built using Object-Oriented Programming (OOP), JSON file storage, and MySQL database integration.

## Features

- Add, search, update, and delete student records
- Store student details and subject-wise marks
- Calculate grades and pass/fail results
- Save and load records using JSON
- Integrate with MySQL for database persistence
- Handle database transactions and errors
- Maintain application logs
- Automated tests using Python's `unittest` framework

## Technologies Used

- **Language:** Python
- **Database:** MySQL
- **Data Storage:** JSON
- **Libraries:** `mysql-connector-python`
- **Testing:** `unittest`

## Project Structure

```text
StudentsManagement/
├── StudentApp/
│   ├── __init__.py
│   ├── manager.py
│   ├── mysql_storage.py
│   ├── storage.py
│   └── student.py
├── tests/
│   ├── test_manager.py
│   ├── test_mysql_storage.py
│   ├── test_storage.py
│   └── test_student.py
├── main.py
├── .gitignore
└── README.md
```

## Requirements

- Python installed
- MySQL Server
- Git (optional, for version control)

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/VenkateshBasker/Student-Management-System.git
   ```

2. Open the project directory:

   ```bash
   cd Student-Management-System
   ```

3. Install the required package:

   ```bash
   python -m pip install mysql-connector-python
   ```

4. Create a MySQL database named `student_management` and configure the required tables.

5. Configure the database connection using environment variables:

   - `DB_HOST`
   - `DB_USER`
   - `DB_PASSWORD`
   - `DB_NAME`

   Never commit database passwords or other credentials to GitHub.

## Run the Application

From the project root, run:

```bash
python main.py
```

## Run Tests

Run the test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

## Purpose

This project demonstrates Python OOP, modular application design, data persistence, SQL database integration, exception handling, and automated testing.