# Explain the syntax of a function definition using the `def` keyword. Why is the colon (`:`) mandatory?

# Function Definition Syntax using `def`
    # A function definition tells Python that a new function is being created.
    # The `def` keyword is used to define a function, followed by function name and parameters.
    # The colon (`:`) marks the start of the function body.

# Syntax of Function Definition:
def function_name(parameters):
    function body

# Important Points
    # `def` keyword starts the function definition.
    # Function name should follow identifier rules.
    # Parameters are optional and written inside parentheses.
    # Colon (`:`) is mandatory at the end of the function header.
    # Function body must be indented (usually 4 spaces).
    # Indentation defines the scope of the function.

# Why is the Colon (`:`) Mandatory?
    # Colon tells Python that a new indented block is starting.
    # It separates the function header from the function body.
    # Python uses indentation instead of `{}` like other languages.
    # Without `:`, Python cannot identify the function block.

# Example 1: Simple function definition
def greet():
    print("Hello World")
greet() # Hello World

# Example 2: Function with parameters
def add(a, b):
    return a + b
print(add(10, 20)) # 30

# Common Mistakes / Interview Points:
    # Missing colon (`:`) causes `SyntaxError`.
    # Missing indentation causes `IndentationError`.