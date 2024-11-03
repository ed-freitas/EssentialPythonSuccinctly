import threading
import time

def perform_task(name, delay):
    print(f"Starting task {name}...")
    time.sleep(delay)  # Simulates a blocking operation
    print(f"Finished task {name} after {delay} seconds.")

# Creating threads
thread1 = threading.Thread(target=perform_task, args=("Thread 1", 2))
thread2 = threading.Thread(target=perform_task, args=("Thread 2", 3))

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print("Both threads have completed.")
