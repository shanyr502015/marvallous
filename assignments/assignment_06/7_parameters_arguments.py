# What is the difference between parameters and arguments in Python functions?

# Key Idea 
    # Parameters are variables defined in the function definition.
    # Arguments are the actual values passed to the function when calling it.
    # Parameters receive the values of arguments during function execution.

# Important Points
    # Parameters are written inside the function definition.
    # Arguments are written inside the function call.
    # Parameters act as placeholders for data.
    # Arguments are real values supplied by the user or program.
    # One parameter receives one argument value.
    # The number of arguments should match the number of parameters (unless defaults are used).

# Example 1: Simple parameters and arguments
def add(a, b):        # a, b are parameters
    return a + b      # function returns sum of a and b

result = add(10, 20)  # 10, 20 are arguments
print(result)         # 30

# Example 2: Parameter receiving different arguments
def greet(name):         # name is a parameter
    print("Hello", name) # name will hold the argument value

greet("Durga")           # "Durga" is an argument
greet("Python")          # "Python" is an argument

# Common Mistakes
    # Saying parameters and arguments are the same (they are not).
    # Confusing function definition time vs function call time.
    # Interview point: “Parameters are formal, arguments are actual.”
