# Why strings are immutable in Python
    # Strings cannot be changed after they are created.
    # This makes strings safe to share in memory.
    # Python can reuse string objects to save memory.
    # Immutability makes strings hashable, so they can be used dictionary keys.

# What happens internally when you modify a string?
s = "Python"
s = s + "3"
# Step-by-step:
    # "Python" is stored in memory.
    # "3" is another string.
    # Python creates a new string "Python3".
    # Variable s now points to the new string "Python3".
    # The old "Python" string remains unchanged (and may be freed later).
# NOTE: The original string is never modified.

# REMEMBER: 
    # Strings immutable in Python to ensure safety, memory efficiency & fast performance. 
    # When string modified, Python creates new string object instead of changing original one.

# This is for me to remember:
# There is NO “old s” and “new s” variable. There is only ONE variable: s. # What changes is what s points to in memory, not the variable itself.
# GOLDEN RULE: When we “modify” a string, Python creates a new string and makes  variable point to it; the old string stays unchanged.