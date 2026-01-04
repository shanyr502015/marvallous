# id(x) returns the unique identity (ID) of the object stored in memory.
# Is id() same for two variables holding the same value? --> Both yes & no — depends on whether both variables point to same object.

# integers (same)
a = 10
b = 10
print(id(a), id(b)) # 140707662493080 140707662493080 (same)
# Because integers are immutable & python reuses them.

# lists (not same)
a = [10]
b = [10]
print(id(a), id(b))   # 1921708439808 1921708322752 (different)
# Because each list is a new object.