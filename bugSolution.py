def function_with_uncommon_error_solution(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Invalid input type: both inputs must be numbers")
    result = a / b
    return result

# Example usage
result1 = function_with_uncommon_error_solution(10, 2)  # Output: 5.0

try:
    result2 = function_with_uncommon_error_solution(10, 0) 
    print(result2) # This line won't execute due to exception
except ZeroDivisionError as e:
    print(f"Caught error: {e}")

try:
    result3 = function_with_uncommon_error_solution(10, "hello") 
    print(result3) # This line won't execute due to exception
except TypeError as e:
    print(f"Caught error: {e}") 