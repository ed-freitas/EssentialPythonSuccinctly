import asyncio

async def fetch_data(delay, name):
    print(f"Starting task {name}...")
    await asyncio.sleep(delay)  # Simulates a long-running I/O-bound task
    print(f"Finished task {name} after {delay} seconds.")
    return f"Data from {name}"

async def main():
    # Schedule both tasks to run concurrently
    task1 = asyncio.create_task(fetch_data(2, "Task 1"))
    task2 = asyncio.create_task(fetch_data(3, "Task 2"))

    print("Waiting for tasks to complete...")
    results = await asyncio.gather(task1, task2)
    print("All tasks completed:", results)

# Run the asyncio event loop
asyncio.run(main())
