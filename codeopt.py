import timeit

# Using list comprehension
def squares_list(n):
    """Generates a list of squares using list comprehension."""
    return [i ** 2 for i in range(n)]

# Using generator
def squares_generator(n):
    """Generates squares one at a time using a generator."""
    for i in range(n):
        yield i ** 2

# Measure time for list comprehension
list_time = timeit.timeit("squares_list(1000000)", setup="from __main__ import squares_list", number=1)
print("List comprehension time:", list_time)

# Measure time for generator
generator_time = timeit.timeit("list(squares_generator(1000000))", setup="from __main__ import squares_generator", number=1)
print("Generator time:", generator_time)
