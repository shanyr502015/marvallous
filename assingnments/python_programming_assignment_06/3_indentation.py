# What is the importance of indentation inside a function body? What happens if indentation is incorrect?

# Indentation in Python Functions
    # Indentation in Python is used to define blocks of code.
    # Inside a function, indentation tells Python which statements belong to that function.
    # Without correct indentation, Python cannot understand the program structure.

# mportant Points (bullets):
    # Python uses indentation instead of braces `{}`.
    # Function body must be indented after `def` and `:`.
    # All statements inside a function should have same indentation level.
    # Common indentation is 4 spaces.
    # Indentation defines the scope of the function.

# Why Indentation is Important Inside a Function:
    # It clearly separates function code from outside code.
    # It tells Python where the function starts and ends.
    # It improves code readability.
    # It avoids logical and syntax errors.

# What Happens if Indentation is Incorrect?
    # Python raises an IndentationError.
    # Program will not execute.
    # Sometimes logic errors occur if indentation is wrong but valid.

# Example 1: Correct indentation
def greet():
    print("Hello")
    print("Welcome")
greet()
# Hello
# Welcome

# Example 2: Incorrect indentation
def greet():
print("Hello") #IndentationError: expected an indented block


# Common Mistakes / Interview Points:
    # Mixing tabs and spaces causes indentation errors.
    # Missing indentation after `:` gives error.