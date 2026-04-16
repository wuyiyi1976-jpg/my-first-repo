def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is undefined. Please provide a non-zero divisor."
    except TypeError:
        return "Error: Invalid input types. Please provide numbers for division."

# Example usage
print(divide(10, 0))
print(divide(10, 'a'))
print(divide(10, 2))