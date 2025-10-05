# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling.
    Returns a message string with either the result or the error.
    """
    try:
        # Try converting to floats
        num = float(numerator)
        den = float(denominator)

        # Try performing division
        result = num / den
        return f"The result of dividing {num} by {den} is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
