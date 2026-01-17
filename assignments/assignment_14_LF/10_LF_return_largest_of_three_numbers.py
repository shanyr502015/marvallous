largest = lambda x, y, z: max(x, y, z)
# usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
result = largest(num1, num2, num3)
print("Largest:", result)

# Alternative
largest = lambda x, y, z: x if (x > y and x > z) else (y if y > z else z)
print(largest(10, 25, 15))  # Output: 25