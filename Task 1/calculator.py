# Simple Calculator - CODSOFT Task 1
# Developer: [Mohamed Amin]
# Performs basic arithmetic operations: +, -, *, /

# Ask the user to enter an operator
operator = input("Enter an operator (+ - * /): ")

# Try converting inputs to numbers
try:
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    # Check the operator and perform the calculation
    if operator == "+":
        result = num1 + num2
        print("Result:", round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print("Result:", round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print("Result:", round(result, 3))
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", round(result, 3))
    else:
        print(f"{operator} is not a valid operator.")

except ValueError:
    print("Please enter valid numbers.")
