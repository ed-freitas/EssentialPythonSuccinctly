import pdb  # Import the pdb module

def divide_numbers(a, b):
    pdb.set_trace()  # Set a breakpoint
    result = a / b
    return result

# Run the function
divide_numbers(10, 2)  # Try with valid input to see how pdb works
