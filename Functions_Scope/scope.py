# Session 10 - Variable Scope

# 1. Local vs global scope
x = 10  # Global variable


def modify_x():
    x = 5  # Local variable
    print("Inside function:", x)


modify_x()
print("Outside function:", x)


# 2. Using the global keyword
def modify_global_x():
    global x
    x = 20
    print("Inside function (global):", x)


modify_global_x()
print("Outside function (modified):", x)
