num = int(input("Enter a number: "))

total = 0
for i in range(1, num + 1):
    total += i

print(total)

# Alternative using formula
num = int(input("Enter a number: "))
total = num * (num + 1) // 2
print(total)