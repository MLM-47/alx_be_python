# This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division)
num1 =  int(input("Enter the first number:"))
num2 =  int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")


match operation:
    case "+":
        print("The result is", num1 + num2)
    case "-":
        print("The result is", num1 - num2)
    case "*":
        print("The result is", num1 * num2)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero. Please enter a value higher than zero.")
        else:
            print("The result is", num1 / num2)
    case _:
        print("Enter a valid number/operator.")
