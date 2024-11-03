import csv

# Writing to a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["Alice", 30, "USA"])
    writer.writerow(["Bob", 25, "UK"])

# Reading from a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
