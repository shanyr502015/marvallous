is_even = lambda x: x % 2 == 0
# usage
num = int(input("Enter a number: "))
result = is_even(num)
print(result)  # Output: True or False

# Alternative
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))   # Output: True
print(is_even(7))   # Output: False