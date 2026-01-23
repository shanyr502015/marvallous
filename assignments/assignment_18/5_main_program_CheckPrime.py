"""
Program: Accept N numbers and return sum of all prime numbers
This program demonstrates modular programming with a user-defined module

File Structure:
1. MarvellousNum.py - Module containing CheckPrime() function
2. main.py - Main program file with ListPrime() function

Input: Number of elements : 11
Input Elements: 13   5   45   7   4   56   10   34   2   5   8
Output: 54 (13 + 5 + 7 + 2 + 5)
"""
# ============================================================
# FILE 2: main.py (Main Program)
# ============================================================
from MarvellousNum_CheckPrime import *

def ListPrime(numbers_list):
    prime_sum = 0
    for num in numbers_list:
        if CheckPrime(num):
            prime_sum += num
    return prime_sum

def main():
    try:
        # Get number of elements from user
        n = int(input("Number of elements: "))
        
        # Get list elements from user
        numbers_list = []
        print(f"Enter {n} elements:")
        for i in range(n):
            num = int(input(f"Element {i + 1}: "))
            numbers_list.append(num)
        
        # Calculate sum of prime numbers
        result = ListPrime(numbers_list)
        
        # Display prime numbers for verification
        prime_numbers = [num for num in numbers_list if CheckPrime(num)]
        print(f"Prime numbers: {' '.join(map(str, prime_numbers))}")
        print(f"Output: {result}")
        
    except ValueError as ve:
        print(f"Error: Please enter valid integer numbers - {ve}")
    except TypeError as te:
        print(f"Error: Type error occurred - {te}")
    except KeyboardInterrupt:
        print("\nError: Program interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()


# ============================================================
# INSTRUCTIONS FOR ACTUAL IMPLEMENTATION:
# ============================================================
"""
To implement this properly with separate files:

1. Create MarvellousNum.py with:
   def CheckPrime(n):
       if n < 2:
           return False
       if n == 2:
           return True
       if n % 2 == 0:
           return False
       for i in range(3, int(n ** 0.5) + 1, 2):
           if n % i == 0:
               return False
       return True

2. Create main.py with:
   from MarvellousNum import CheckPrime
   
   def ListPrime(numbers_list):
       prime_sum = 0
       for num in numbers_list:
           if CheckPrime(num):
               prime_sum += num
       return prime_sum
   
   # ... rest of main() function ...

3. Run: python main.py
"""