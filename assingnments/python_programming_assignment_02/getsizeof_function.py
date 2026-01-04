# getsizeof() function 
    # returns memory size of an object in bytes.occupied by the object.
    # It help to understand memory consumption/usage,  different between data types and performance considerations.
    # It is useful for writing memory-efficient programs.

# getsizeof() is available in the sys module.
import sys
x = 10
y = 3.14
z = [1, 2, 3]
print(sys.getsizeof(x)) #28 (may vary based on system and python implementation)
print(sys.getsizeof(y)) #24 (may vary based on system and python implementation)
print(sys.getsizeof(z)) #88 (may vary based on system and python implementation)

# Why is memory size different for different data types?
    # different data types store data in different internal formats.
    # Some data types store only one value, while others store multiple values.
    # more information stored → more memory required.