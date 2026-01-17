is_odd = lambda x: x % 2 != 0
#  usage
num = int(input("Enter a number: "))
result = is_odd(num)
print(result)  # Output: True or False

# Alternative
is_odd = lambda x: True if x % 2 != 0 else False
print(is_odd(5))   # Output: True
print(is_odd(8))   # Output: False