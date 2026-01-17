num = int(input("Enter a number: "))

for i in range(1, num + 1, 2):
    print(i, end=" ")


# Alternative approach
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if i % 2 != 0:
        print(i, end=" ")