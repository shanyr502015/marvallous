# print is used to display output on the screen.
# return is used to send a value back to the caller.
# A function can work without print, but useful functions usually use return.

# print Statement: Used to show output to the user.
# Important Points:
    # Displays value on console.
    # Does not send value back.
    # Mainly for debugging or display.
    # Function ends after print, but returns None.

# Example 1: Using print
def add(a, b):
    print(a + b)
x = add(10, 20)
print(x)  # Output: 30
          # Output: None
# Example 2: Only display
def greet():
    print("Hello") # This function only prints, does not return a value
greet() # Output: Hello

# return StatementUsed to send result back to the function caller.
# Important Points:
    # Returns value to calling code.
    # Can be stored in a variable.
    # Stops function execution immediately.
    # One function can return multiple values (tuple).

# Example 1: Using return
def add(a, b):
    return a + b
x = add(10, 20)
print(x)
# Example 2: Return stops execution
def test():
    return 10
    print("Hi")   # never executes
print(test())

# ---------------------------------------------------
# | print                   | return               |
# | ----------------------- | -------------------- |
# | Displays output         | Sends value back     |
# | Used for showing result | Used for computation |
# | Returns `None`          | Returns actual value |
# | Cannot be reused        | Can be reused        |
# ------------------------- | -------------------- |

#  When to Use print vs return:
    # Use print for simple output display.
    # Use return for functions that compute and provide results.

# Using print instead of return in logic-based functions.
    # Interview Q: “Can we use both?” → Yes, but for different purposes.
    # Interview Q: “Which is better?” → return for reusable logic.