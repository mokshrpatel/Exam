import pytest

@pytest.fixture
def total_student():
    return 10

def test_full_attendance(total_student):
    present = 10
    assert present == total_student
    
def test_partial_attendance(total_student):
    present = 8
    assert present > 0 and present < total_student
    
def test_zero_clases(total_student):
    present = 0
    assert present == 0
    
def test_invalid_values(total_student):
    present = -1
    assert present < 0 or present > total_student