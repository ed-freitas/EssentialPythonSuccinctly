# Variables
#
name = "Alice"  # String variable
anotherName = 'Alice'  # String variable
age = 30  # Integer variable
height = 5.5  # Float variable
is_student = True  # Boolean variable

print("Name:", name)
print("Another Name:", anotherName)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Lists
#
# A list is an ordered collection of items.
fruits = ["apple", "banana", "cherry"]

# Accessing elements in a list
print("First fruit:", fruits[0])

# Adding elements to a list
fruits.append("mango")
print("Fruits after adding date:", fruits)

# For loop
for fruit in fruits:
    print("Fruit:", fruit)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Conditionals
# Conditionals allow you to execute different code based on conditions.

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Functions
# A function is a reusable block of code that performs a specific task.

def greet(name):
    """Greet a person by their name."""
    return f"Hello, {name}!"

print(greet("Bob"))

# Function with multiple parameters and default parameter value
def add(a, b=5):
    """Add two numbers."""
    return a + b

print("Add 3 + 4:", add(3, 4))
print("Add 3 + default 5:", add(3))

# Dictionaries
# A dictionary is a collection of key-value pairs.

person = {
    "name": "Charlie",
    "age": 28,
    "city": "New York"
}

# Accessing elements in a dictionary
print("Person's name:", person["name"])

# Adding elements to a dictionary
person["email"] = "charlie@example.com"
print("Person dictionary after adding email:", person)

# Tuples
# A tuple is an ordered, immutable collection of items.

coordinates = (10.0, 20.0)

# Accessing elements in a tuple
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Classes
# A class defines a blueprint for creating objects.

class Dog:
    """A simple class representing a dog."""
    
    def __init__(self, name, age):
        """Initialize the dog with a name and age."""
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says woof!"

# Creating an instance of the Dog class
my_dog = Dog("Rex", 5)

# Accessing attributes and methods
print("Dog's name:", my_dog.name)
print("Dog's age:", my_dog.age)
print(my_dog.bark())

dogs = [Dog("Buddy", 3), Dog("Bella", 2), Dog("Max", 1)]

for dog in dogs:
    print(dog.name, "is", dog.age, "years old.")