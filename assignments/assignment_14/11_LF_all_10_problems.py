# Problem 1: Square of a number
square = lambda x: x ** 2
# Problem 2: Cube of a number
cube = lambda x: x ** 3
# Problem 3: Maximum of two numbers
maximum = lambda x, y: x if x > y else y
# Problem 4: Minimum of two numbers
minimum = lambda x, y: x if x < y else y
# Problem 5: Check if number is even
is_even = lambda x: x % 2 == 0
# Problem 6: Check if number is odd
is_odd = lambda x: x % 2 != 0
# Problem 7: Check if divisible by 5
divisible_by_5 = lambda x: x % 5 == 0
# Problem 8: Addition of two numbers
addition = lambda x, y: x + y
# Problem 9: Multiplication of two numbers
multiplication = lambda x, y: x * y
# Problem 10: Largest of three numbers
largest = lambda x, y, z: max(x, y, z)


# Testing all lambda functions
print("=" * 50)
print("LAMBDA FUNCTIONS - ALL SOLUTIONS")
print("=" * 50)

print("\n--- Problem 1: Square ---")
print("Square of 5:", square(5))

print("\n--- Problem 2: Cube ---")
print("Cube of 3:", cube(3))

print("\n--- Problem 3: Maximum ---")
print("Maximum of 10 and 20:", maximum(10, 20))

print("\n--- Problem 4: Minimum ---")
print("Minimum of 10 and 20:", minimum(10, 20))

print("\n--- Problem 5: Check Even ---")
print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))

print("\n--- Problem 6: Check Odd ---")
print("Is 5 odd?", is_odd(5))
print("Is 8 odd?", is_odd(8))

print("\n--- Problem 7: Divisible by 5 ---")
print("Is 10 divisible by 5?", divisible_by_5(10))
print("Is 7 divisible by 5?", divisible_by_5(7))

print("\n--- Problem 8: Addition ---")
print("5 + 3 =", addition(5, 3))

print("\n--- Problem 9: Multiplication ---")
print("4 × 5 =", multiplication(4, 5))

print("\n--- Problem 10: Largest of Three ---")
print("Largest of 10, 25, 15:", largest(10, 25, 15))

print("\n" + "=" * 50)