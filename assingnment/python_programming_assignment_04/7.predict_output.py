d = {1: "One", 1: "ONE", 2: "Two"}
print(d)  # Output: {1: 'ONE', 2: 'Two'}

# Explaination
    # In dictionary, keys must be unique.
    # Here, key 1 is written twice:
        # first: 1: "One"
        # second: 1: "ONE"
    # Python keeps only last value for duplicate key.
    # So "One" is overwritten by "ONE" for key 1.
    # That’s why final dictionary becomes: {1: 'ONE', 2: 'Two'}