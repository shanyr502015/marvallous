num = int(input("Enter a number: "))
count = 0
temp = num

while temp > 0:
    temp = temp // 10
    count += 1

print(count)

# Alternative using string conversion
num = int(input("Enter a number: "))
count = len(str(num))
print(count)