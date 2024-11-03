from memory_profiler import profile

@profile
def generate_large_list(n):
    """Function that generates a large list of squares from 1 to n."""
    large_list = [i ** 2 for i in range(n)]
    return large_list

# Run the function with profiling
generate_large_list(1000000)
