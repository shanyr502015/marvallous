num = int(input("Enter a number: "))

divisible_by_3 = (num % 3 == 0)
divisible_by_5 = (num % 5 == 0)

if divisible_by_3 and divisible_by_5:
    print(f"Divisible by 3 and 5")
elif divisible_by_3:
    print(f"Divisible by 3")
elif divisible_by_5:
    print(f"Divisible by 5")
else:
    print(f"Not divisible by 3 or 5")