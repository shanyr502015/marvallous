# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934                  Output : 37

def SumDigits(n):
    n = abs(n)  # Handle negative numbers
    sum_digits = 0
    
    while n > 0:
        digit = n % 10
        sum_digits += digit
        n //= 10
    
    return sum_digits

def main():
    num = int(input("Enter number: "))
    result = SumDigits(num)
    print(f"Sum of digits in {num} is: {result}")

if __name__ == "__main__":
    main()