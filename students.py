# Comprehensive example combining dictionaries and classes

class Student:
    """A class representing a student."""

    def __init__(self, name, grades):
        """Initialize the student with a name and grades."""
        self.name = name
        self.grades = grades  # Dictionary of subject: grade
    
    def average_grade(self):
        """Calculate the average grade of the student."""
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count if count > 0 else 0

students = [
    Student("Alice", {"math": 90, "science": 85, "english": 88}),
    Student("Bob", {"math": 75, "science": 80, "english": 70}),
    Student("Charlie", {"math": 95, "science": 100, "english": 90}),
]

for student in students:
    print(f"{student.name}'s average grade is {student.average_grade()}")
