def basic_calculator():
    """
    A simple Python function that performs a basic arithmetic operation 
    (addition, subtraction, multiplication, or division) on two user-input numbers.
    """
    print("Welcome to the Basic Calculator!")

    # 1. Get the first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # 2. Get the operation
    while True:
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if operation in ('+', '-', '*', '/'):
            break
        else:
            print("Invalid operation. Please enter +, -, *, or /.")

    # 3. Get the second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            
            # Check for division by zero
            if operation == '/' and num2 == 0:
                print("Error: Cannot divide by zero. Please enter a different second number.")
                continue
            
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # 4. Perform the calculation and print the result
    result = None
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Division by zero is already handled above, but this is a safeguard
        if num2 != 0:
            result = num1 / num2
    
    # Print the formatted result
    if result is not None:
        print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    basic_calculator()