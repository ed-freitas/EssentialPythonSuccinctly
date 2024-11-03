from collections import deque

# Initialize a deque with some elements
dq = deque([1, 2, 3, 4, 5])

# Append elements to the right and left ends
dq.append(6)
dq.appendleft(0)

# Pop elements from the right and left ends
dq.pop()
dq.popleft()

print("Final deque state:", dq)