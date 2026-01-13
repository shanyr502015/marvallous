# What is the role of the pass statement in a function definition?

# Key Idea 
    # The `pass` statement is used as a placeholder in a function body.
    # It allows you to define a function with no implementation for now.
    # Python requires at least one statement inside a function block.

# Important Points
    # `pass` does nothing when executed.
    # Used when the function logic is not yet decided.
    # Prevents syntax errors in empty function definitions.
    # Often used during planning or testing stages.
    # Can be replaced later with actual code.

# Example 1: Empty function using pass
def my_function():
    pass
print(my_function())  # None

# Example 2: Function to be implemented later
def calculate_salary():
    pass  # logic will be added later
# Calling the function
result = calculate_salary()
print(result)  # None

# Common Mistakes
    # Forgetting `pass` in an empty function causes `IndentationError`.
    # `pass` is not the same as `return`.
    # `pass` does not stop execution; it just skips action.
    # Frequently asked: “Why is pass needed in Python?”
