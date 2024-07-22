# debug_code.py

# Challenge: Debug the Code
# Here is a code snippet with a bug. Identify and fix the bug.

def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)

# Identify the bug and explain the issue:
# The bug is ______________________________________________________________

# Fixed Code:
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

result = divide(10, 0)
print(result)
