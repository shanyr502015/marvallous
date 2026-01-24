"""Design a Python application that creates two threads named Prime and NonPrime.
• Both threads should accept a list of integers.
• The Prime thread should display all prime numbers from the list.
• The NonPrime thread should display all non-prime numbers from the list."""

import threading
# Create a lock for synchronized printing
print_lock = threading.Lock()

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def Prime(numbers):
    """Display all prime numbers from the list"""
    prime_numbers = []
    
    # Find all prime numbers
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    
    # Lock ensures complete output before another thread prints
    with print_lock:
        print("\nPrime thread started")
        print(f"Prime numbers: {prime_numbers}")
        print("Prime thread completed")

def NonPrime(numbers):
    """Display all non-prime numbers from the list"""
    non_prime_numbers = []
    
    # Find all non-prime numbers
    for num in numbers:
        if not is_prime(num):
            non_prime_numbers.append(num)
    
    # Lock ensures complete output before another thread prints
    with print_lock:
        print("\nNonPrime thread started")
        print(f"Non-prime numbers: {non_prime_numbers}")
        print("NonPrime thread completed")

def main():
    # Get list of integers from user
    print("Enter integers separated by spaces:")
    user_input = input()
    numbers = list(map(int, user_input.split()))
    
    print(f"\nInput list: {numbers}")
    
    # Create two threads
    t1 = threading.Thread(target=Prime, args=(numbers,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(numbers,), name="NonPrime")
    
    # Start both threads
    t1.start()
    t2.start()
    
    # Wait for both threads to complete
    t1.join()
    t2.join()
    
    print("\nBoth threads completed execution")

if __name__ == "__main__":
    main()