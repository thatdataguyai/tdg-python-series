import os
from pathlib import Path

# Creating a new directory
os.makedirs("test_directory", exist_ok=True)

# Create then write to a file
file_path = Path("test_directory/sample.txt")
with open(file_path, "w") as file:
   file.write("Hello World!")

# Reading the file
with open(file_path, "r") as fle:
   print("File contents:", file.read())

# Checking that a file exists
if file_path.exists():
    print(f"{file_path} exists")

# Delete the file and directory
file_path.unlink()
os.rmdir("test_directory")
print("Cleanup Complete...")