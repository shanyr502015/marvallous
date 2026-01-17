minimum = lambda x, y: x if x < y else y

# usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = minimum(num1, num2)
print("Minimum:", result)

# Alternative
minimum = lambda x, y: min(x, y)
print(minimum(10, 20))  # Output: 10