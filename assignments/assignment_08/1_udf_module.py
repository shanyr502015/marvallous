# Creating and Using a User-Defined Module
# A user-defined module is essentially a Python file containing functions, classes, or variables that you can reuse in other programs. 

# Creating a Module
# Step 1: Write your Python code
# Create a new `.py` file with the functions or classes you want to reuse. 
# For example, create a file called `mymodule.py`: mymodule.py
def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b
PI = 3.14159
# Step 2: Save the file
# Save it in a directory where Python can find it (typically the same folder as your main program, or in Python's module search path).
## Using the Module
# Step 3: Import the module
# In your main program, you can import and use the module in several ways:
# Method 1: Import entire module
import mymodule
print(mymodule.greet("Alice"))
print(mymodule.add(5, 3))
# Method 2: Import specific items
from mymodule import greet, PI
print(greet("Bob"))
print(PI)
# Method 3: Import with alias
import mymodule as mm
print(mm.add(10, 20))
# Method 4: Import everything (not recommended)
from mymodule import *
print(add(7, 8))
# Important Notes
# - The module file must be in the same directory as your program or in Python's `sys.path`
# - Module names should be valid Python identifiers (no spaces, start with letter)
# - Python automatically compiles modules to `.pyc` files for faster loading
# - You can organize related modules into packages (folders with an `__init__.py` file)

################################################## Why is from module import * discouraged in professional code? ###############################################
################################################################################################################################################################
    # Namespace Pollution: It imports everything from the module into your current namespace, making it unclear where functions/variables come from when reading the code.
    # Name Conflicts: If the module contains a function named open() or list(), it will override Python's built-in functions, causing hard-to-debug errors.
    # Readability Issues: Other developers (or future you) won't know which names come from which module without checking the module's contents.
    # Hidden Dependencies: It's unclear what exactly you're using from the module, making refactoring and maintenance difficult.
    # Better Practice: Explicitly import what you need: from module import function1, function2 or use import module and access items as module.function1().

#################################### How does modular programming improve code reusability, testing, and maintenance? #########################################
###############################################################################################################################################################
    # Reusability:
        # Write once, use anywhere—modules can be imported into multiple projects
        # Reduces code duplication and development time
        # Creates a library of tested, reliable components
    # Testing:
        # Each module can be tested independently (unit testing)
        # Isolates functionality, making bugs easier to locate
        # Mock dependencies easily during testing
        # Reduces test complexity by testing small, focused units
    # Maintenance:
        # Changes to one module don't necessarily affect others (loose coupling)
        # Bugs are isolated to specific modules, easier to fix
        # Code is organized logically, easier to navigate
        # Multiple developers can work on different modules simultaneously

#################################### What happens internally when Python executes an import module_name statement? ###########################################
##############################################################################################################################################################
# Python follows these steps:
    # Search: Python searches for the module in locations defined in sys.path (current directory, PYTHONPATH, standard library)
    # Check Cache: Python checks sys.modules dictionary to see if the module was already imported (to avoid re-importing)
    # Load: If not cached, Python locates the .py file and reads it
    # Compile: Python compiles the source code to bytecode (creates .pyc file in __pycache__ directory)
    # Execute: Python executes the module's code from top to bottom in its own namespace
    # Create Module Object: Python creates a module object and populates it with the module's functions, classes, and variables
    # Cache: The module object is stored in sys.modules for future imports
    # Bind: The module name is bound in the current namespace, allowing you to access it

#################################### What happens if a module contains print statements outside any function? ################################################
##############################################################################################################################################################
# They execute immediately when the module is imported for the first time.
# Example: # mymodule.py
print("Module is being loaded!")  # Executes on import
def my_function():
    print("Function called")

# main.py
import mymodule  # Prints: "Module is being loaded!"
import mymodule  # Prints nothing (already cached)
mymodule.my_function()  # Prints: "Function called"
# Key Points:
    # Top-level code runs only once (on first import)
    # Subsequent imports use the cached version
    # This is why modules often use if __name__ == "__main__": to separate executable code from importable code
    # Can be useful for initialization but should be used carefully

#################################### Why are Python modules considered the foundation of scalable software design? ##########################################
#############################################################################################################################################################
    # Separation of Concerns: Each module handles a specific functionality, making complex systems manageable by breaking them into logical components.
    # Abstraction: Modules hide implementation details, exposing only necessary interfaces—changes to internal code don't affect users of the module.
    # Code Organization: Large projects become navigable hierarchies rather than monolithic files, making them easier to understand and manage.
    # Team Collaboration: Different teams can work on different modules independently with clear interfaces, enabling parallel development.
    # Dependency Management: Clear module boundaries make it easier to understand and manage dependencies between components.
    # Scalability: New features can be added as new modules without modifying existing ones, and systems can grow from small scripts to large applications.
    # Versioning and Updates: Individual modules can be updated, versioned, or replaced without affecting the entire system.
    # Performance: Only needed modules are loaded, reducing memory footprint and startup time.
# Modules are the building blocks that allow Python applications to scale from simple scripts to enterprise-level systems like Instagram, Dropbox, and YouTube.