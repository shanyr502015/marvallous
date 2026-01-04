# Write a function that does not return anything but prints a message. Explain the default return value of such a function.

def greet_user():
    print("Hello! Welcome to Python programming.") # Hello! Welcome to Python programming.

# greet_user()
# explanation: function greet_user() prints a message, It does not use return statement. So, function does not return any value explicitly.

# Default return value of such a function: In python, if function does not return anything, it automatically returns None (means no value).

def greet_user():
    print("Hello! Welcome to Python programming.")

result = greet_user()
print(result)
# explanation: When greet_user() is called, it prints message. Since there is no return statement, it returns None by default. So, print(result) outputs None.