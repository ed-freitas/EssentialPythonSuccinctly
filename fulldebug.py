import logging
import pdb

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')

def divide_numbers(a, b):
    pdb.set_trace()  # Set breakpoint for debugging
    
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        print("Error: Cannot divide by zero.")
    except TypeError:
        logging.error("Invalid types provided for division.")
        print("Error: Please enter numeric values.")
    except Exception as e:
        logging.exception("An unexpected error occurred.")
        print("An unexpected error occurred.")

# Testing different scenarios
divide_numbers(10, 2)    # Successful division
divide_numbers(10, 0)    # Division by zero
divide_numbers(10, 'a')  # Type error
