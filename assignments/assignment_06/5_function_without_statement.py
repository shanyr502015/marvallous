# Question:Can a Python function exist without any statements inside its body? If yes, how?

# Key Idea
    # Yes, a Python function can exist without any executable statements.
    # In such cases, the `pass` keyword is used as a placeholder.
    # `pass` tells Python that the function body is intentionally empty.

# Important Points (bullets):
    # Python does not allow an empty function body.
    # `pass` is a null statement (does nothing).
    # Used when function logic is not decided yet.
    # Helps avoid `IndentationError`.
    # Common in function stubs and future planning.

# How Can a Function Exist Without Statements?**
    # By using the `pass` keyword inside the function body.
    # `pass` satisfies Python’s syntax rules.
    # Function can be defined now and implemented later.

# Example_1: Empty function using pass
def test():
    pass
print("Function defined successfully") # Function defined successfully

# Example_2: pass used as placeholder
def calculate():
    pass   # logic will be added later
calculate() # No output, but function exists

# What Happens Without `pass`?
# If a function is defined without any statements, Python raises an `IndentationError`.
def fun():
# No statement here # IndentationError: expected an indented block

# Common Mistakes
    # Forgetting `pass` causes `IndentationError`.
    # Interview Q: “Why is pass needed?” → To define empty blocks.
    # `pass` does nothing, but is syntactically required.
