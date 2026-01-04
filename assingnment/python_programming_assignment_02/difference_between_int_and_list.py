a = 10
b = 10
print(id(a)) # 140707662493080
print(id(b)) # 140707662493080
# integers: Same value/Same memory, id(a) == id(b)

a = [10]
b = [10]
print(id(a)) # 1376853211392
print(id(b)) # 1376853094336
# lists: same value/different memory, id(a) != id(b)

# so, python shares memory for integers, but creates new memory for each list