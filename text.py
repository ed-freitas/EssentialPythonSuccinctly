# Writing to a text file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("File handling is essential in Python.\n")

# Reading from a text file
with open("example.txt", "r") as file:
    content = file.read()  # Read the entire file content
    print(content)