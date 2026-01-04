# 1)Mutability
# List - Mutable: we can change it (add/remove/update)
lst = [1, 2, 3]
lst[0] = 10
# Tuple - Immutable: we cannot change it once created
tup = (1, 2, 3)
tup[0] = 10  # This will raise an error
# --------------------------------------------------

# 2) Memory
# List uses more memory because it keeps extra space for changes (mutable)/(growing/shrinking).
# Tuple  uses less memory than list because it is fixed (immutable)/(not growing/not shrinking).
import sys
print(sys.getsizeof([1,2,3]))
print(sys.getsizeof((1,2,3)))
# --------------------------------------------------

#3) Performance
# List is slightly slower because it supports modifications (mutable)/(growing/shrinking).
# Tuple is usually faster to access/iterate than list (immutable)/(not growing/not shrinking).
import timeit   
list_time = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)
print(f"List creation time: {list_time}")       
print(f"Tuple creation time: {tuple_time}")
# --------------------------------------------------

# 4) Use cases
# Use List when: Data will change, we need to add/remove items. Example: marks list, shopping cart etc.
# Use Tuple when: Data should not change, we want fixed records. Example: coordinates `(x, y)`, RGB color `(255, 0, 0)`,database row etc.
## Quick table (easy to remember)
