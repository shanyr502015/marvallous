radius = float(input("Enter radius of circle: "))

pi = 3.14159
area = pi * radius * radius

print("Area of circle:", area)


# Alternative using math module:
import math

radius = float(input("Enter radius of circle: "))
area = math.pi * radius ** 2
print("Area of circle:", area)