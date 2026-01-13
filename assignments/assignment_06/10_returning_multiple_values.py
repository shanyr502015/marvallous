# Can a Python function return multiple values? If yes, how does Python handle it internally?

# Key Idea 
    # Yes, a Python function can return multiple values.
    # Internally, Python packs multiple return values into a tuple.
    # The caller can unpack this tuple into multiple variables.

# Important Points
    # Multiple values are returned using a single `return` statement.
    # Values are separated by commas in the `return`.
    # Python automatically creates a tuple behind the scenes.
    # The returned tuple can be unpacked into variables.
    # If not unpacked, the result is a tuple object.

# Example 1: Returning multiple values
def calc(a, b):
    return a + b, a - b
result = calc(10, 5)
print(result)        # (15, 5)
print(type(result))  # <class 'tuple'>

# Example 2: Tuple unpacking of return values
def calc(a, b):
    return a * b, a / b
mul, div = calc(10, 2)
print(mul)  # 20
print(div)  # 5.0

# Common Mistakes
    # Thinking Python returns multiple values separately (it returns a tuple).
    # Forgetting to unpack the returned tuple.
    # Interview point: “Multiple return values are packed into a tuple internally.”

# Micro Practice Questions:
    # 1. What is the data type of multiple returned values?
    # 2. What happens if you assign multiple return values to one variable?
    # 3. Write a function that returns min and max of two numbers.
