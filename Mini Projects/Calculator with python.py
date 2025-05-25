import math  # Importing math module for advanced mathematical operations

# Define a function to add two numbers
def add(a, b):
    return a + b

# Define a function to subtract second number from first
def subtract(a, b):
    return a - b

# Define a function to multiply two numbers
def multiply(a, b):
    return a * b
    
# Define a function to divide first number by second
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"  # Handle division by zero
    return a / b

# Define a function to raise a to the power of b
def power(a, b):
    return a ** b

# Define a function to get modulus of a by b
def modulus(a, b):
    return a % b

# Define a function to compute square root
def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"  # Handle invalid input
    return math.sqrt(a)
    
