from src.student_app.services.calculator import get_status


def display_report(student):
    print("\nStudent Report")
    print("----------------")
    print(f"Name: {student.name}")
    print(f"Marks: {student.marks}")
    print(f"Grade: {student.grade}")
    print(f"Status: {get_status(student.grade)}")
