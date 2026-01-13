# What is dynamic typing in Python?
    # Dynamic typing means you do not declare a variable’s data type in advance.
    # Python automatically decides data type based on value assigned.
    # same variable can hold different data types at different times during execution.

x = 10
print(type(x))   # int

x = 10.5
print(type(x))   # float

x = "Python"
print(type(x))   # str

x = [1, 2, 3]
print(type(x))   # list 

x = (1, 2, 3)
print(type(x))   # tuple

x = {1, 2, 3}
print(type(x))   # set

x = {'a': 1, 'b': 2}
print(type(x))   # dict

x = True
print(type(x))   # bool

x = None
print(type(x))   # NoneType

# In Python,we can reassign variables to different data types without any restrictions.