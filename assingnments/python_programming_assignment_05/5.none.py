# None in Python?
    # None represents no value or nothing.
    # It is a special constant in Python.
    # The data type of None is NoneType.
    # It is commonly used when a variable has no value or a function does not return anything
x = None
print(x)          # None
print(type(x))    # <class 'NoneType'>

def func():
    return None 
print(func())          # None
print(type(func()))    # <class 'NoneType'>

# A function that does not explicitly return a value returns None by default.
if None:
    print("True")
else:
    print("False")   # False
# In conditional statements, None is treated as False.