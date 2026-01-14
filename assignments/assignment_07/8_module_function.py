# A function is a block of code that performs a single specific task.
# A module is a file (.py) that contains related code like functions, variables, and classes.
# Functions are inside modules; modules help in organizing large programs.

# Important Points
# Function:
    # Defined using `def`.
    # Performs one task.
    # Cannot exist independently outside a module/file.
    # Called/invoked to execute its code.

# Module:
#   A Python file containing reusable code.
#   Can include multiple functions, variables, and classes.
#   Imported using `import` or `from ... import`.
# One module can contain many functions.
# Modules improve code reusability and maintainability.


# Example 1: Function example
def add(a, b):
    return a + b
print(add(10, 20))
# Output: 30

# Example 2: Module example
# file name: math_ops.py
def add(a, b):
    return a + b
def sub(a, b):
    return a - b

# using the module
import math_ops
print(math_ops.add(10, 5))
# Output: 15

# Common Mistakes
    # ❌ Thinking module and function are the same.
    # ❌ Forgetting that a module is a file, not a block of code.
    # Interview point: Every Python program itself is a module.

# ✅ Yes, a module can exist without any functions.
# A module may contain:
    # Only variables
    # Only classes
    # Only executable statements
    # Or even nothing (empty file).
    # There is no limit on how many functions a module can contain.
    # A module can contain any number of functions, based on requirement.
    # In real projects, modules usually group related functions.

# How many functions can a module contain?
# 👉 Any number. There is no restriction.


#Extra Recommended Methods 
# Built-in modules – `math`, `sys`, `os`
# `__name__ == "__main__"` – controls module execution
# Packages – collection of modules in a folder
# `dir(module)` – list module members