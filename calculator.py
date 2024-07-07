# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Function to perform exponentiation
def power(x, y):
    return x ** y

# Function to perform modulo operation
def modulus(x, y):
    return x % y

# Main function to run the calculator
def calculator():
    print("Welcome to Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Modulus")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5/6): ")

    # Check if choice is one of the options
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} ** {num2} = {power(num1, num2)}")
        elif choice == '6':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
    else:
        print("Invalid input. Please enter a valid number.")

# Run the calculator function
calculator()
