# Session 17 - Reading from Files

# 1. Reading a file
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print("File not found!")

# 2. Reading line by line
try:
    with open("sample.txt", "r") as file:
        print("Reading line by line:")
        for line in file:
            print(line.strip())  # .strip() removes leading/trailing whitespace
except FileNotFoundError:
    print("File not found!")
