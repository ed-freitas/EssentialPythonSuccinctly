from multiprocessing import Process
import time

def compute_square(numbers):
    print(f"Calculating squares...")
    for n in numbers:
        time.sleep(1)  # Simulates a heavy computation delay
        print(f"Square of {n}: {n * n}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Creating a separate process for compute_square
    process = Process(target=compute_square, args=(numbers,))
    
    process.start()  # Start the process
    process.join()   # Wait for the process to complete

    print("All computations are completed.")
