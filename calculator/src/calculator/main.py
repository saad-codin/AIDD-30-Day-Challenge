import re
import sys

def evaluate_expression(expression: str) -> float:
    if not expression:
        raise ValueError("Invalid expression: Expression cannot be empty")

    # Corrected regular expression to match basic arithmetic operations and numbers (integers and floats)
    # Allows for optional spaces around operators
    # Captures: (1) first operand, (2) operator, (3) second operand
    pattern = re.compile(r"^(-?\d+(?:\.\d+)?)\s*([-+*/])\s*(-?\d+(?:\.\d+)?)$")

    match = pattern.match(expression)
    if not match:
        raise ValueError("Invalid expression: Only basic arithmetic operations (e.g., '2+2', '5*3.1') are supported")

    try:
        # Extract operands and operator using corrected groups
        operand1 = float(match.group(1))
        operator = match.group(2)
        operand2 = float(match.group(3))
    except ValueError:
        raise ValueError("Invalid expression: Could not parse operands")
    except IndexError:
        # This can happen if regex match is unexpected or groups are wrong
        raise ValueError("Invalid expression: Could not extract parts")


    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero")
        return operand1 / operand2
    else:
        # This case should ideally not be reached due to the regex
        raise ValueError("Invalid operator")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m calculator.main \"<expression>\"")
        sys.exit(1)

    expression_to_evaluate = sys.argv[1]
    try:
        result = evaluate_expression(expression_to_evaluate)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
