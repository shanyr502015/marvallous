# What is the Boolean data type in Python?
    # The Boolean data type represents True or False.
    # It is used for decision making and conditions.
    # Boolean values belong to the data type bool.

a = True
b = False
print(type(a))   # <class 'bool'>
a = True
b = False
print(type(a))   # <class 'bool'>
print(a and b)   # False
print(a or b)    # True 

# Boolean values in Python: Python has only two Boolean values:
    # True
    # False

print(not a)     # False
print(not b)     # True

# List all values that evaluate to False: following values are considered False when used in conditions:
    # False
    # None
    # 0 (zero)
    # 0.0
    # "" (empty string)
    # [] (empty list)
    # () (empty tuple)
    # {} (empty dictionary)
    # set() (empty set)