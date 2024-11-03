import json

# Writing to a JSON file
data = {
    "name": "Alice",
    "age": 30,
    "is_employee": True,
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading from a JSON file
with open("data.json", "r") as file:
    data_loaded = json.load(file)
    print(data_loaded)
