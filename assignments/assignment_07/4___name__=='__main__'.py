# `__name__` is a built-in variable in every Python file.
# Its value depends on how the Python file is used.
# It helps Python decide whether a file is run directly or imported as a module.

# Important Points
    # When a Python file is executed directly: `__name__` value is `"__main__"`.
    # When the same file is imported as a module: `__name__` value is the module name (file name).
    # Code inside:`if __name__ == "__main__":` runs only when file is executed directly.
    # This prevents unwanted code execution during import.
    # Very important for **real projects and interviews.

# Example 1: Executed directly
# file name: test.py
print(__name__)
# Output when run directly:
# __main__

# Example 2: Direct execution vs import
# file name: demo.py
def add(a, b):
    return a + b
if __name__ == "__main__":
    print(add(10, 20)) # Output when running demo.py directly → 30
    
# importing demo.py in another file

# file name: use_demo.py
import demo
# Output:
# When running demo.py directly → 30
# When importing demo.py → nothing prints
# because the code inside `if __name__ == "__main__":` does not execute.
# Direct Explanation of Values:
    # Executed directly:`__name__ = "__main__"`
    # Imported as module:`__name__ = "<module_name>"`

# Why do we write if __name__ == "__main__": in Python?
    # This condition is used to control code execution.
    # It ensures that certain code runs only when the file is executed directly.
    # It prevents that code from running when the file is **imported as a module.