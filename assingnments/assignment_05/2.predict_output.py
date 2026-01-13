b = bytes([65, 66, 67])
print(b) # b'ABC'
print(type(b)) # <class 'bytes'>

# How numbers are converted internally (simple words)
    # bytes([...]) takes list of numbers.
    # Each number must be between 0 to 255.
    # Python converts each number to its ASCII character:
        # 65 → 'A'
        # 66 → 'B'
        # 67 → 'C'
    # Then it makes a bytes object: b'ABC'
# NOTE:Python converts each number (0–255) into its corresponding ASCII character & forms bytes object.