# What happens if the number of arguments passed does not match the function parameters?

# Key Idea 
    # If the number of arguments passed does not match the function parameters, Python raises an error.
    # This usually happens when too few or too many arguments are given.
    # Python checks this at function call time.

# Important Points 
    # If fewer arguments are passed → `TypeError` occurs.
    # If more arguments are passed → `TypeError` occurs.
    # Error message clearly mentions missing or extra arguments.
    # This rule applies to normal parameters (without defaults).
    # Default parameters can avoid this error in some cases.

# Example 1: Fewer arguments than parameters
def add(a, b):
    return a + b
add(10)  # TypeError: add() missing 1 required positional argument: 'b'

# Example 2: More arguments than parameters
def greet(name):
    print("Hello", name)
greet("Durga", "Soft")  # TypeError: greet() takes 1 positional argument but 2 were given

# Common Mistakes
    # Forgetting to pass all required arguments.
    # Passing extra values by mistake.
    # Interview point: Python strictly checks parameter–argument matching.