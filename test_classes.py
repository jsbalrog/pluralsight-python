import pytest
from classes import Student


@pytest.fixture
def student():
    return Student("bruce")


def test_create(student):
    assert student.name == "bruce"
    assert student.student_id == 332


def test_capitalize(student):
    assert student.get_name_capped() == "Bruce"


def test_school_name(student):
    assert student.get_school_name() == "Springfield Elementary"
