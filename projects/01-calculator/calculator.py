# Calculator project

print("Simple Calculator")

try:
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            exit()
        result = num1 / num2
    else:
        print("Error: Invalid operation.")
        exit()

    print(f"\nResult: {result}")

except ValueError:
    print("Error: Please enter valid numbers.")