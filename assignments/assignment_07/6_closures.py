# Closures in Python (Inner Function Remembers Outer Variables)

# Key Idea
    # A closure is a function that remembers variables from its outer function, even after the outer function has finished execution.
    # The inner function can use outer variables without redefining them.
    # This happens because Python stores those variables in the function’s closure memory.

# Important Points (bullets):
# A closure is created when:
#   There is a **nested function.
#   The inner function uses outer function variables.
#   The outer function returns the inner function.
# Outer variables are not destroyed after the outer function call.
# Closures help in data hiding and state preservation.
# Used commonly in decorators and factory functions.

# Code Examples:
# Example 1: Basic closure
def outer():
    x = 10
    def inner():
        return x
    return inner
f = outer()
print(f())
# Output: 10

# Example 2: Closure with parameter
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply
double = multiplier(2)
print(double(5))
# Output: 10

# Common Mistakes
    # ❌ Thinking outer variables are deleted after function execution.
    # ❌ Modifying outer variable without `nonlocal` keyword.
    # Interview point: Closures store values in cell objects, not global memory.

# Extra Recommended Methods / Topics (not in your original passage):
# `nonlocal` keyword – modify outer variable inside inner function
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

# Closures vs Global variables – safer and cleaner design
# Closures in decorators – core interview concept