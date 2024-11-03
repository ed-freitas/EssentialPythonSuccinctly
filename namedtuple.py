from collections import namedtuple

# Define a namedtuple type for a point in 2D space
Point = namedtuple("Point", ["x", "y"])

# Create instances of Point
p1 = Point(3, 4)
p2 = Point(5, 9)

# Access the fields
print("Point 1:", p1)
print("Point 1 x coordinate:", p1.x)
print("Point 2 y coordinate:", p2.y)