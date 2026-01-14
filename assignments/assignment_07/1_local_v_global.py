# There is local keyword in python but there is global keyword in python.
# Water in local fridge , water in public or global drinking panpoi.

# What is the difference between local variables and global variables?

# Local variables
#   Declared inside a function.
#   Scope is limited to that function only.
#   Created when the function is called and destroyed after it ends.
#   Safer and easier to manage.
def fun(): # local variable
    x = 10      # local variable
    print(x) # print local variable
fun() # 10
print(x)  # Error: x is not defined

# Global variables
#   Declared outside all functions.
#   Accessible throughout the program.
#   Exists as long as the program runs.
#   Can be modified by functions (using `global` keyword).
x = 10   # global variable
def fun():
    print(x)
fun()
print(x)

# Why should excessive use of global variables be avoided in large programs?

    # Makes code hard to understand and debug.
    # Any function can change the value unexpectedly.
    # Reduces reusability of functions.
    # Causes side effects and bugs.
    # Not thread-safe in multi-threaded programs.
    # Difficult to maintain in large projects.

# Explain the use of the `global` keyword. When should it be used?

#  `global` keyword is used to modify a global variable inside a function.
#  Without `global`, Python treats the variable as local.
x = 10
def fun():
    global x
    x = 20  # modifies global variable
fun()
print(x)  # 20
# When to use `global`:
    # When a function must update a global variable.
    # Use it rarely and carefully.
    # Prefer function arguments and return values instead of globals.

# Better approach (avoid global)
def fun(x):
    return x + 10
x = 10
x = fun(x)
print(x)   # 20