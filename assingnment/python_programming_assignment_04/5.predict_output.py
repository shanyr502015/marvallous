s = "Python"
print(id(s)) # 2177322975888

s = s + "3"
print(id(s)) # 2177323143776

# Why does id(s) change?
    # Strings are immutable (cannot be changed).
    # When we do: s = s + "3", Python creates a new string object "Python3" in memory. Then variable s is updated to point to this new object.
# So:
    # First id(s) → ID of "Python"
    # Second id(s) → ID of "Python3"
    # IDs are different because objects are different.

# NOTE: id(s) changes because string concatenation creates new string object, and s is reassigned to it.