def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Both inputs must be numeric."

    try:
        result = num / denom
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."