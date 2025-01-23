# Session 7 - Nested Loops and Pattern Printing

# 1. Simple pattern using nested loops
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# 2. Inverted triangle pattern
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# 3. Number pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 4. Nested loops with lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
