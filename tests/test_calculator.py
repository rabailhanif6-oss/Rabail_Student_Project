from src.student_app.services.calculator import calculate_grade, get_status


def test_grade_a():
    assert calculate_grade(85) == "A"


def test_grade_b():
    assert calculate_grade(75) == "B"


def test_grade_c():
    assert calculate_grade(65) == "C"


def test_grade_d():
    assert calculate_grade(55) == "D"


def test_grade_f():
    assert calculate_grade(40) == "F"


def test_status_pass():
    assert get_status("A") == "Pass"


def test_status_fail():
    assert get_status("F") == "Fail"
