# What is the special variable `__name__` in Python? Who assigns its value?
    #  `__name__` is a special built-in variable in Python.
    # It stores the name of the current module.
    # Python automatically creates and assigns this variable.

# Values of `__name__`:
# If a Python file is **run directly,`__name__` value is `"__main__"`.
# If a Python file is **imported as a module, `__name__` value is the **module name (file name)**.

# Who assigns its value?
# The Python interpreter assigns the value of `__name__`.

# file: test.py
print(__name__)
# Output when run directly:__main__

# file: demo.py
import test
#  Output when imported: test

# Use of `__name__ == "__main__"`:
    # Used to control execution of code.
    # Ensures some code runs only when the file is executed directly, not when imported.

def main():
    print("Main function")

if __name__ == "__main__":
    main()
# When run directly, prints "Main function".
# When imported, does not print anything.   