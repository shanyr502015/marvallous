
# Dictionary is data type in python used to store data in key–value pairs. Example: student = {"name": "Shantaram", "age": 38}
# -------------------------------------------------------------------

# 1) Key–value pair 
    # Key = name to find data
    # Value = actual data stored
    # Example: {"name": "Shantaram"} , here "name"  -> key  &  "Shantaram" -> value
# We access value using key:
student = {"name": "Shantaram", "age": 38}
print(student["name"])   # Shantaram
print(student["age"])    # 38
# -------------------------------------------------------------------

# 2) Why keys must be immutable
    # Dictionary uses key to find value.
    # For this, key must have fixed value (cannot change).
    # Immutable types like `str`, `int`, `tuple` are safe keys.

# Allowed keys (immmutable key like int, string, tuple): d = {1: "one", "a": 10, (1,2): "tuple"}
# Not allowed (mutable key like list): d = {[1,2]: "list"}  # error
    # Reason: If a key changes, Python won’t be able to find the value correctly.
# -------------------------------------------------------------------

# 3) Why duplicate keys are not allowed

# Keys must be unique so each key points to only one value.
# If we repeat key, Python will keeplast value & overwrite old one.

# Example: 
d = {"a": 1, "a": 2}
print(d) # Output: {'a': 2}
# Reason: One key cannot store two different values at same time.



# NOTE: A dictionary stores data as key–value pairs; keys must be immutable so they remain stable for lookup, and duplicate keys are not allowed because each key must uniquely map to one value.
