# range(start,stop,end)
# built-in type used to representsequence of numbers.
# mostly used in loops.
# It generates numbers like: 0, 1, 2, 3 ... based on start, stop, step.
#------------------------------------------

# Syntax:
r = range(1, 6)   # 1 to 5
print(r)          # Output: range(1, 6)
print(list(r))    # Output: [1, 2, 3, 4, 5] 
#------------------------------------------

# How is range different from a list of numbers?
# 1) Storage (main difference)
    # range does not store all numbers in memory.
    # It stores only start, stop, step and produces numbers when needed.
    # A list stores all numbers in memory.
# 2) Memory
    # range uses less memory.
    # List uses more memory.
# 3) Output display
    # range prints like: range(1, 6)
    # List prints like: [1, 2, 3, 4, 5]
#------------------------------------------

# Example:
print(range(1, 6))        # range(1, 6)
print(list(range(1, 6)))  # [1, 2, 3, 4, 5]