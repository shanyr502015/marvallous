# Difference between bytes & bytearray

# 1) Mutability
# bytes: Immutable --> cannot changed after creation
b = b"ABC"
# b[0] = 68   # ❌ error
print(b[0]) # 65

# bytearray: Mutable --> can changed after creation
ba = bytearray(b"ABC")
ba[0] = 68     # changes 'A' to 'D'
print(ba)      # bytearray(b'DBC')
print(ba[0])   # 68

# 2) Use cases
# Use bytes when:
    # Data should not change
    # Reading files / images / network data safely
    # Using as dictionary keys (because immutable)
# Use bytearray when:
    # We need to modify binary data.
    # Editing file bytes, encryption/decryption buffers, streaming data


# NOTE: bytes immutable & used for fixed binary data, while bytearray mutable & used when we need to modify binary data.
