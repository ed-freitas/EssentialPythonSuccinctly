import os
import shutil

# Create a new directory
os.makedirs("test_dir/sub_dir", exist_ok=True)

# Create a new file in the directory
with open("test_dir/sample.txt", "w") as file:
    file.write("This is a sample file.")

# Move the file to a new location
shutil.move("test_dir/sample.txt", "test_dir/sub_dir/sample.txt")

# Copy the file to a new location
shutil.copy("test_dir/sub_dir/sample.txt", "test_dir/sample_copy.txt")

# Delete the file and directory
os.remove("test_dir/sample_copy.txt")
shutil.rmtree("test_dir")  # Deletes test_dir and all its contents
