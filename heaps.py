import heapq

# Create a list of unsorted numbers
numbers = [20, 5, 15, 10, 30]

# Convert the list to a heap
heapq.heapify(numbers)
print("Heapified list:", numbers)

# Add a new number to the heap
heapq.heappush(numbers, 7)
print("Heap after adding 7:", numbers)

# Pop the smallest element
smallest = heapq.heappop(numbers)
print("Smallest element:", smallest)
print("Heap after popping smallest element:", numbers)
