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
# FILE 1: MarvellousNum_CheckPrime.py (User-defined Module)
# ============================================================
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