numbers = [3, 5, 10, 15, 20, 30, 45, 60]
divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print("Numbers divisible by both 3 and 5:", divisible)
# Output: [15, 30, 45, 60]