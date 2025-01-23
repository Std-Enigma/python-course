# Session 28 - Regular Expressions

import re

# 1. Searching for a pattern
pattern = r"\d+"  # Match one or more digits
text = "My phone number is 123-456-7890."

match = re.search(pattern, text)
if match:
    print("Found number:", match.group())

# 2. Finding all matches
matches = re.findall(pattern, text)
print("All numbers found:", matches)
