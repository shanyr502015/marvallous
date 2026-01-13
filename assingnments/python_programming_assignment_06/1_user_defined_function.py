# What is a user-defined function in Python? Why do we need functions instead of writing code repeatedly?
    # A user-defined function is a function written by the programmer using the `def` keyword.
    # It groups a set of statements into a single unit that can be reused many times.
    # Functions help avoid rewriting the same code again and again.

# Important Points (bullets):
    # Defined using the `def` keyword.
    # A function can be called multiple times.
    # Helps reduce code repetition.
    # Improves readability and maintainability.
    # Makes debugging and testing easier.
    # Supports modular programming (divide big program into small parts).

# Why Do We Need Functions Instead of Rewriting Code?
    # To avoid duplication of code.
    # To save time and effort.
    # To make code reusable.
    # To improve clarity of the program.
    # To change logic at one place instead of many places.

# Example 1: Simple user-defined function
def greet():
    print("Hello, Welcome to Python")

# Calling the function multiple times
greet() # Hello, Welcome to Python
greet() # Hello, Welcome to Python

# Example 2: Function with parameters
def add(a, b):
    return a + b
# Calling the function with different arguments
result = add(10, 20)
print(result) # 30

# Common Mistakes / Interview Points
    # Forgetting to call the function after defining it.
    # Indentation errors inside function body.
    # Function definition runs only when it is called.