# Session 6 - Loops (for and while)

# # 1. Using a for loop
print("Counting from 1 to 5:")
for i in range(6):
    print(i)

# 2. Using a while loop
print("Countdown from 5 to 1:")
count = 5
while count > 0:
    print(count)
    count -= 1
    pass

# 3. Loop control: break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# 4. Loop control: continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

for c in "Hello":
    print(c)

# 5. Looping through a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
