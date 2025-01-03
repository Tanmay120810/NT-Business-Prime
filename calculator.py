# Improved Calculator Program

def calculator():
    print("\nWelcome to the Python Calculator!")
    print("=================================")

    # Input for user name
    name = input("Enter your Name: ").strip()
    print(f"Hello {name}, the calculator is ready to use!\n")

    while True:
        try:
            # Input for numbers and operation
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nSelect an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            operation = input("Enter the symbol of the operation (+, -, *, /): ").strip()

            # Perform the selected operation
            if operation == "+":
                result = num1 + num2
                print(f"\nResult: {num1} + {num2} = {result}\n")
            elif operation == "-":
                result = num1 - num2
                print(f"\nResult: {num1} - {num2} = {result}\n")
            elif operation == "*":
                result = num1 * num2
                print(f"\nResult: {num1} * {num2} = {result}\n")
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"\nResult: {num1} / {num2} = {result}\n")
                else:
                    print("\nError: Division by zero is not allowed!\n")
            else:
                print("\nInvalid operation. Please select a valid symbol (+, -, *, /).\n")

        except ValueError:
            print("\nError: Please enter a valid number.\n")

        # Ask user if they want to continue
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThank you for using the Python Calculator. Goodbye!")
            break

# Run the calculator function
calculator()
# ©2024 Code-With-Parashar Company | All Rights Reserved.