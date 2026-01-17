maximum = lambda x, y: x if x > y else y

# usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = maximum(num1, num2)
print("Maximum:", result)

# Alternative
maximum = lambda x, y: max(x, y)
print(maximum(10, 20))  # Output: 20