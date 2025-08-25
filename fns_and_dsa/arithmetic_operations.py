# def perform_operation(num1, num2, operation):
#     match operation:
#         case "add":
#             result = num1+num2
#         case "subtract":
#             result = num1-num2
#         case "multiply":
#             result = num1*num2
#         case "divide":
#             if num2 == 0:
#                 result = "Zero division is not allowed."
#             else:
#                 result = num1/num2
#         case _:
#             raise "invalid input."
#     return result


def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            result = "Zero division is not allowed."
        else:
            result = num1 / num2
    else:
        raise ValueError("Invalid input.")
    return result
