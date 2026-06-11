scores = {
    'math': 95,
    'science': 73,
    'english': 61
}

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

# These will crash without proper error handling
print(calculate_average([85, 90, 78]))   # Works fine
print(calculate_average([]))             # ZeroDivisionError
print(calculate_average(None))           # TypeError