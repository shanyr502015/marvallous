# What is a return value in a function?

# Key Idea 
    # A return value is the result that a function sends back to the caller.
    # It is returned using the `return` statement.
    # The returned value can be stored in a variable or used directly.

# Important Points
    # `return` sends data from a function to the calling code.
    # A function can return any type of value (int, float, string, list, etc.).
    # If `return` is not used, the function returns `None` by default.
    # Code written after `return` will not be executed.
    # A function can return multiple values using commas.

# Example 1: Function returning a value
def add(a, b):
    return a + b
result = add(10, 20)
print(result)  # 30

# Example 2: Function without return statement
def greet(name):
    print("Hello", name)
value = greet("Durga")
print(value)   # None

# Common Mistakes 
    # Forgetting to use `return` and expecting a value.
    # Confusing `print()` with `return`.
    # Interview point: `print` displays output, `return` sends value.

# Micro Practice Questions:**
    # 1. What does a function return if there is no `return` statement?
    # 2. Write a function that returns the square of a number.
    # 3. Can a function return more than one value?