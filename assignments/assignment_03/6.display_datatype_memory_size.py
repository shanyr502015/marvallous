import sys

value = input("Enter any value: ") # Enter any value: shantaram

# Display data type
print("Data type:", type(value)) # Data type: <class 'str'>
# Display memory address
print("Memory address (id):", id(value)) # Memory address (id): 258820074864
# Display size in bytes
print("Size in bytes:", sys.getsizeof(value)) # Size in bytes: 50


# input(): takes value from user
# type(): shows data type
# id(): shows memory address
# sys.getsizeof(): shows memory size in bytes