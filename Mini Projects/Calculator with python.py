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
    
# Define a function to compute factorial of a number
def factorial(n):
    if n < 0:
        return "Error: Cannot compute factorial of negative number"  # Handle negative input
    if not float(n).is_integer():
        return "Error: Factorial is only defined for integers"  # Factorial must be an integer
    return math.factorial(int(n))  # Convert float to int before computing

# Main function to run the calculator
def run_calculator():
    print("=========== Calculator ===========")  # Welcome message
    print("Available operations: add, subtract, multiply, divide, power, modulus, square_root, factorial\n(type 'exit' to quit)")
    
    while True:  # Start a loop to read commands from user
        user_input = input("> ").strip().lower()  # Read input, remove leading/trailing spaces, convert to lowercase
        if user_input == "exit":
            print("Goodbye!")  # Exit message
            break  # Exit loop and terminate
