def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        return f"The result of the division is: {num / denom}"
    except ValueError:
        return "Error: Please enter numerical values only."
    except ZeroDivisionError as e:
        return str(e)
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"