# Function Returning Another Function (Higher-Order Functions)

# Key Idea:
    # Yes, in Python, a function can return another function.
    # Functions are treated as objects, just like numbers or strings.
    # This is possible because Python supports **first-class functions.

# Important Points:
    # A function can be created inside another function.
    # The inner function can be returned without calling it.
    # The returned function can be stored in a variable and called later
    # This concept is used in closures, decorators, and factory functions.


# Example 1: Simple function returning another function
def outer():
    def inner():
        return "Hello from inner function"
    return inner
f = outer()      # outer returns inner function
print(f())       # calling returned function
# Output: Hello from inner function

# Example 2: Function returning function with data
def power(n):
    def calculate(x):
        return x ** n
    return calculate

square = power(2)
print(square(5))     # 5^2
# Output: 25

# Common Mistakes 
    # ❌ Writing `return inner()` instead of `return inner` (this calls the function).
    # Interview point: This is possible because functions are first-class objects.
    # Used heavily in decorators.