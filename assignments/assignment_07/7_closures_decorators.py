# Closures and decorators are NOT the same, but they are closely related.
# A closure is a concept where an inner function remembers outer variables.
# A decorator is a practical application built using closures.
# All decorators use closures, but not all closures are decorators.

# Important Points (bullets):

# Closure:
#   Remembers outer function variables.
#   Focuses on data/state preservation.
#   Can exist without modifying another function.

# Decorator:
#   A function that takes another function as input.
#   Returns a new modified function.
#   Used to add extra behavior without changing original code.
# Decorators internally use closures to remember the original function.

# Interview rule: Decorator = function + closure + callable wrapping.

# Example 1: Closure (no decorator)
def outer(msg):
    def inner():
        return msg
    return inner

f = outer("Hello")
print(f())
# Output: Hello


# Example 2: Decorator (uses closure internally)
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()
# Output:
# Before function call
# Hello
# After function call


# Common Mistakes 
# ❌ Saying closures and decorators are the same.
# ❌ Forgetting that decorators must accept a function as argument.
# ❌ Not returning the inner function in decorators.
# ❌ Assuming all closures are decorators.

# Interview Q: Are decorators possible without closures?
# 👉 No, closures are required to remember the wrapped function.

# Micro Practice Questions:

# 1. Can a closure exist without a decorator?
# 2. Why does a decorator need to return a function?
# 3. Write a decorator that prints function name before execution.

# Extra Recommended Methods / Topics 
# Decorator with arguments – nested closures
def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

# `functools.wraps` – preserves function metadata
# Multiple decorators – execution order matters
# Context Managers with decorators – using `contextlib`
