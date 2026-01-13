lst = [10, 20, 30]
tpl = (10, 20, 30)

lst[0] = 100
print( lst) # Output: [100, 20, 30]
    # lst is a list
    # Lists are mutable
    # So this line works
    # List becomes: [100, 20, 30]

tpl[0] = 100 # TypeError: 'tuple' object does not support item assignment
    # tpl is a tuple
    # Tuples are immutable
    # So this line raises an error