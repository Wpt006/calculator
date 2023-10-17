import calculator
from calculator import *

def calculate():
  """Performs a calculation based on user input."""

  # Get the user's input
  operation = input("Enter the operation you want to perform (+, -, *, /): ")
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Perform the calculation
  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  elif operation == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operation.")
    return

  # Display the result
  print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
  calculate()