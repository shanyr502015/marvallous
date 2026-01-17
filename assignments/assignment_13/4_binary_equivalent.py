num = int(input("Enter a number: "))

binary = ""
temp = num

if temp == 0:
    binary = "0"
else:
    while temp > 0:
        remainder = temp % 2
        binary = str(remainder) + binary
        temp = temp // 2

print("Binary equivalent:", binary)


# Alternative using built-in function:
num = int(input("Enter a number: "))
binary = bin(num)[2:]  # [2:] removes '0b' prefix
print("Binary equivalent:", binary)