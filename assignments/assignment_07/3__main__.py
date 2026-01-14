# `__main__` represents the starting point of program execution in Python.
# It indicates that a Python file is being executed directly, not imported.

# When a Python program is run, Python sets:__name__ = "__main__"
# This helps Python identify which file is the entry point of execution.

# Example:
print(__name__)
# Output when run directly:__main__
# Output when imported into another file: module_name

# Use of `__main__`:
    # To execute certain code only when the file is run directly.
    # Prevents execution of test or main code when the file is imported.

def main():
    print("Program started")
if __name__ == "__main__":
    main()

# Key Point:
    #  `__main__` is not a function.
    # It is a string value assigned to `__name__` by the Python interpreter.