import logging

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,                       # Minimum level to log
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    filename='app.log',                       # Log output file
    filemode='w'                              # Write mode (overwrites each run)
)

def divide_numbers(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")  # Info log for successful division
        return result
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero.")  # Error log for division by zero
    except TypeError as e:
        logging.error("Invalid types provided for division.")  # Error log for type error
    except Exception as e:
        logging.exception("An unexpected error occurred.")  # Logs exception with traceback

# Testing the logging function
divide_numbers(10, 2)    # Successful division
divide_numbers(10, 0)    # Division by zero
divide_numbers(10, 'a')  # Type error