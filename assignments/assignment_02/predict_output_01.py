a = 10
b = 10
print(id(a) == id(b)) # True (because integers are immutable & python reuses them.) 

# Why this happens?
    # a and b both store value 10.
    # 10 is an integer and integers are immutable (cannot be changed).
    # python reuses same object for small integers like 10 (this is called integer caching).
    # So a and b point to same object in memory.