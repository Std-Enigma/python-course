# Session 4 - Strings and String Manipulation

# 1. String Creation and Indexing
# print("Message:", message)
# print("First character:", message[0])
# print("Last character:", message[-1])
# print("Substring from index 9 to 15:", message[9:15])

# 2. String Methods
message = "Learning Python is fun!"
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Is alphanumeric:", message.isalnum())
print("Count of 'n':", message.count("n"))
print("Replace 'fun' with 'awesome':", message.replace("fun", "awesome"))

# 3. String Concatenation
first_part = "Python "
second_part = "Programming"
full_message = first_part + second_part
print("Concatenated message:", full_message)

# 4. String Formatting
name = "Devil"
language = "Python"
formatted_message = f"Hello, my name is {name} and I am learning {language}."
print(formatted_message)

# 5. Multi-line Strings
long_message = """This is a multi-line string.
You can write across multiple lines.
This is useful for long texts or paragraphs."""
print(long_message)

# 6. Escape Characters
print('Using escape characters: "Quotes", \\Backslash, and \nNewline.')
