num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime Number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime Number")