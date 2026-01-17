from functools import reduce

numbers = [10, 25, 15, 30, 20]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum element:", maximum)
# Output: 30