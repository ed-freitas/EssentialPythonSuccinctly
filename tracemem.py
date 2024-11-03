import tracemalloc

def memory_intensive_task(n):
    """Function that generates a large list of squares from 1 to n and returns it."""
    return [i ** 2 for i in range(n)]

# Start tracking memory
tracemalloc.start()

# Execute the function and get a snapshot
memory_intensive_task(1000000)
snapshot = tracemalloc.take_snapshot()

# Display the top memory blocks
top_stats = snapshot.statistics('lineno')

print("[Top 5 Memory Consumers]")
for stat in top_stats[:5]:
    print(stat)
