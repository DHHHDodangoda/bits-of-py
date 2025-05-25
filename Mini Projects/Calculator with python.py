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

        parts = user_input.split()  # Split the input into command and arguments
        if not parts:
            continue  # Skip empty input


        cmd = parts[0]  # First part is the command
        args = parts[1:]  # Remaining parts are arguments

        try:
            # Match command with expected operations and number of arguments
            if cmd == "add" and len(args) == 2:
                print(add(float(args[0]), float(args[1])))
            elif cmd == "subtract" and len(args) == 2:
                print(subtract(float(args[0]), float(args[1])))
            elif cmd == "multiply" and len(args) == 2:
                print(multiply(float(args[0]), float(args[1])))
            elif cmd == "divide" and len(args) == 2:
                print(divide(float(args[0]), float(args[1])))
            elif cmd == "power" and len(args) == 2:
                print(power(float(args[0]), float(args[1])))
            elif cmd == "modulus" and len(args) == 2:
                print(modulus(float(args[0]), float(args[1])))
            elif cmd == "square_root" and len(args) == 1:
                print(square_root(float(args[0])))
            elif cmd == "factorial" and len(args) == 1:
                print(factorial(float(args[0])))
            else:
                print("Invalid command or wrong number of arguments.")  # Catch invalid commands
        except ValueError:
            print("Error: Please enter valid numeric values.")  # Handle non-numeric input
