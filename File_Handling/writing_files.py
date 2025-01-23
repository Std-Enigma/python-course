# Session 18 - Writing to Files

# 1. Writing to a file
with open("output.txt", "w") as file:
    file.write("This is a sample output file.\n")
    file.write("We are writing data to it.\n")

# 2. Appending to a file
with open("output.txt", "a") as file:
    file.write("Appending more data to the file.\n")

# 3. Reading the written content
with open("output.txt", "r") as file:
    content = file.read()
    print("Content of output.txt:")
    print(content)
