import pytest
import calculator
from calculator import *
from pytest import approx

def test_addition():
    assert add(8,9) == 17

def test_subtraction():
    assert subtract(1,10) == -9

def test_multiplication():
    assert multiply(5,2) == 10

# handles division
# DONE: handles zero division 
def test_division():
    assert divide(8,0) == "Cannot divide by 0"
    assert divide(10,5) == 2

# handles negative
def test_divide_negative():
    assert multiply(10,-2) == -20
    assert multiply(-10,-2) == 20
    assert divide(-10,-2) == 5
    assert divide(-10,2) == -5

# handles division by a floating-point number
def test_divide_float():
    assert divide(10,3) == 10/3

# handles powerOf 
#def test_powerOf():
#    assert powerOf(3,2) == 9

@pytest.mark.parametrize("num1,num2,expectedResult", [(3, 8, 11), (-3, -8, -11), (3, -8, -5)])
def test_Add(num1, num2, expectedResult):
    result = calculator.add(num1, num2)
    assert result == expectedResult

# Testing Multiply Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(7, 5, 35), (-7, -5, 35), (7, -5, -35)])
def test_Multiply(num1, num2, expectedResult):
    result = calculator.multiply(num1, num2)
    assert result == expectedResult

# Testing Division Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(21, 3, 7), (-21, -3, 7), (-21, 3, -7)])
def test_Divide(num1, num2, expectedResult):
    result = calculator.divide(num1, num2)
    assert result == expectedResult
