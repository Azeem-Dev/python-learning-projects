# PYTHON CALCULATOR


operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        print(f"{num1} + {num2} = {round(num1 + num2, 2)}")
    case "-":
        print(f"{num1} - {num2} = {round(num1 - num2, 2)}")
    case "*":
        print(f"{num1} * {num2} = {round(num1 * num2, 2)}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {round(num1 / num2, 2)}")
        else:
            print("Error! Division by zero is not allowed.")
    case _:
        print("Invalid operator. Please try again.")
