import pytest
from employee_data import Employee

@pytest.fixture
def employee():
    """Set up a employee data to test."""
    return Employee('Test', 'User', 50_000)

def test_give_default_raise(employee):
    employee.give_default_raise()
    assert employee.annual_salary == 55_000

def test_give_custom_raise(employee):
    raise_amount = 10_000
    employee.give_custom_raise(raise_amount)
    assert employee.annual_salary == 60_000 
