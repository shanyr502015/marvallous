# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934                  Output : 7s

def CountDigits(n):
    if n == 0:
        return 1
    
    n = abs(n)  # Handle negative numbers
    count = 0
    
    while n > 0:
        count += 1
        n //= 10
    
    return count

def main():
    num = int(input("Enter number: "))
    result = CountDigits(num)
    print(f"Number of digits in {num} is: {result}")

if __name__ == "__main__":
    main()