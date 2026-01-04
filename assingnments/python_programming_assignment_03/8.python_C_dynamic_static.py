# Example dynamic typing in Python
x = 100
# Why this code works in Python without declaration? Python is dynamically typed and automatically understands type of data from value.
print(type(x)) # <class 'int'>
# Here, 100 is an integer, so Python makes x an int.

# Example static typing in  C
# In C, we must declare type of variable before using it. If we don't, we get an error because C is statically typed.
# int x = 100;