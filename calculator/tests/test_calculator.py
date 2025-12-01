import pytest
from calculator.main import evaluate_expression

def test_addition():
    assert evaluate_expression("2+2") == 4
    assert evaluate_expression("2.5+1.5") == 4.0

def test_subtraction():
    assert evaluate_expression("5-3") == 2
    assert evaluate_expression("5.0-1.5") == 3.5

def test_multiplication():
    assert evaluate_expression("2*3") == 6
    assert evaluate_expression("2.5*2") == 5.0

def test_division():
    assert evaluate_expression("6/3") == 2
    assert evaluate_expression("5.0/2.0") == 2.5

def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        evaluate_expression("10/0")

def test_invalid_expressions():
    with pytest.raises(ValueError, match="Invalid expression"):
        evaluate_expression("2++2")
    with pytest.raises(ValueError, match="Invalid expression"):
        evaluate_expression("abc")
    with pytest.raises(ValueError, match="Invalid expression"):
        evaluate_expression("2+*3")
    with pytest.raises(ValueError, match="Invalid expression"):
        evaluate_expression("")

