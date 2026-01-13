# Bytes
    # bytes data type used to store binary data.
    # bytes represent sequence of bytes (numbers from 0 to 255).
    # bytes are written using b prefix.

b = b"Python"
print(b) # b'Python'
print(type(b)) # <class 'bytes'>

# Why are bytes immutable?
    # Once bytes object is created, its content cannot be changed.
    # Immutability improves performance and security.
    # Bytes used for files, images, and network data, where data should not change accidentally.

b = b"ABC"
# b[0] = 68   # ❌ Error: bytes object does not support item assignment
print(b[0]) # 65