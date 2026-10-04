import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import APP_NAME, DEBUG
from logger import logger
from src.student_app.utils.validation import validate_name, validate_marks
from src.student_app.services.calculator import calculate_grade
from src.student_app.reports.student_report import display_report
from src.student_app.models.student import Student

DATA_FILE = PROJECT_ROOT / "data" / "student.json"


def load_student():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    print(f"Starting: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print()

    try:
        student_data = load_student()
    except FileNotFoundError:
        logger.error(f"Missing data file: {DATA_FILE}")
        print("Error: student.json not found.")
        return
    except json.JSONDecodeError:
        logger.error("Malformed JSON in student.json")
        print("Error: student.json is not valid JSON.")
        return

    print("Student Information")
    print("-------------------")
    print(f"ID: {student_data['id']}")
    print(f"Name: {student_data['name']}")
    print(f"Program: {student_data['program']}")
    print(f"Semester: {student_data['semester']}")
    print(f"Marks: {student_data['marks']}")
    print()

    logger.info("Application started")

    name = input("Enter student name: ")
    if not validate_name(name):
        logger.warning("Empty student name entered")
        print("Error: Name cannot be empty.")
        return

    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        logger.error("Invalid marks entered")
        print("Error: Marks must be a number.")
        return

    if not validate_marks(marks):
        logger.warning(f"Invalid marks entered: {marks}")
        print("Error: Marks must be between 0 and 100.")
        return

    grade = calculate_grade(marks)
    student = Student(name, marks, grade)
    display_report(student)


if __name__ == "__main__":
    main()
