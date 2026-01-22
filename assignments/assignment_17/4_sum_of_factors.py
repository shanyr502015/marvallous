# Write a program which accept one number form user and return addition of its factors.
# Input : 12                       Output : 16          (1+2+3+4+6)

def sumfactors(no):
    if no <= 0:
        return 0
    sum_factors = 0
    for i in range(1, no):
        if no % i == 0:
            sum_factors += i
    return sum_factors

def main():
    num = int(input("Enter number: "))
    ret = sumfactors(num)
    print(f"Sum factors of {num} is: {ret}")

if __name__ == "__main__":
    main()