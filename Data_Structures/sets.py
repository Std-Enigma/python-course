# Session 13 - Sets

# 1. Creating a set
colors = {"red", "green", "blue"}
print("Set of colors:", colors)

# 2. Adding and removing elements
colors.add("yellow")
print("After adding yellow:", colors)

colors.remove("green")
print("After removing green:", colors)

# 3. Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
