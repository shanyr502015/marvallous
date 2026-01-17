from functools import reduce

numbers = [10, 25, 15, 30, 20]
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print("Minimum element:", minimum)
# Output: 10