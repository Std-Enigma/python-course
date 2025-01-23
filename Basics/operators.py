# Session 3 - Operators and Expressions

# 1. Arithmetic Operators
a = 2
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a**b)

# 2. Comparison Operators
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("a == b:", a == b)
print("a != b:", a != b)

# 3. Logical Operators
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# 4. Combined Expressions
z = 10
expression_result = (a > b) and (z < a)
print("Combined expression (a > b) and (z < a):", expression_result)

# 5. Operator Precedence
result = 5 + 3 * 2  # Multiplication happens first
print("5 + 3 * 2 =", result)
result_with_parentheses = (5 + 3) * 2  # Parentheses change precedence
print("(5 + 3) * 2 =", result_with_parentheses)
