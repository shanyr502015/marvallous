
# Why does the `input()` function always return string?
    # input() takes data typed from keyboard.
    # Whatever we type (number, word, symbol) is read text. 
    # In Python, text is called string.
    # So, input() always returns string.

x = input("Enter number: ")
print(type(x)) # <class 'str'>

# How can you convert it to another data type? By using type conversion functions.

# Convert to integer:
x = int(input("Enter a number: "))
print(type(x)) # <class 'int'>

# Convert to float:
x = float(input("Enter a number: "))
print(type(x)) # <class 'float'>
