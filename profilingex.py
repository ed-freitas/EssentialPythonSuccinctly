import timeit

# Sum squares with a for loop
def sum_squares_loop(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Sum squares with a generator expression
def sum_squares_generator(n):
    return sum(i ** 2 for i in range(n))

# Measure time for loop
loop_time = timeit.timeit("sum_squares_loop(1000000)", setup="from __main__ import sum_squares_loop", number=1)
print("Loop time:", loop_time)

# Measure time for generator expression
generator_time = timeit.timeit("sum_squares_generator(1000000)", setup="from __main__ import sum_squares_generator", number=1)
print("Generator expression time:", generator_time)
