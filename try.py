def divide_numbers(a, b):
    try:
        # Attempt to divide a by b
        result = a / b
        print(f"The result is {result}")
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero.")
    except TypeError:
        # Handle incorrect data types error
        print("Error: Both inputs must be numbers.")
    else:
        # This block runs if no exceptions were raised
        print("Division successful.")
    finally:
        # This block always runs, even if an exception occurred
        print("End of division operation.")

# Testing divide_numbers function
divide_numbers(10, 2)   # Normal division
divide_numbers(10, 0)   # Division by zero
divide_numbers(10, 'a') # Type error
