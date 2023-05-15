# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    return a / b

# Dictionary of operations
operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}

# List of operation names
operation_names = ['Add', 'Subtract', 'Multiply', 'Divide']

# Main program loop
while True:
    print("Select an operation:")
    for i, name in enumerate(operation_names):
        print(f"{i + 1}. {name}")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the program...")
        break

    if choice not in operations:
        print("Invalid choice. Please try again.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. input must be a Number")
        continue

    operation = operations[choice]
    result = operation(num1, num2)
    print("Result:", result)
