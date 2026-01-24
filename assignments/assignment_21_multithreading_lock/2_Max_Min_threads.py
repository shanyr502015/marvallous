"""Design a Python application that creates two threads.
• Thread 1 should calculate and display the maximum element from a list.
• Thread 2 should calculate and display the minimum element from the same list.
• The list should be accepted from the user."""

import threading
# Create a lock for synchronized printing
print_lock = threading.Lock()

def find_maximum(numbers):
    """Calculate and display the maximum element from the list"""
    max_element = max(numbers)
    
    # Lock ensures complete output before another thread prints
    with print_lock:
        print("\nThread 1 started")
        print(f"Maximum element: {max_element}")
        print("Thread 1 completed")

def find_minimum(numbers):
    """Calculate and display the minimum element from the list"""
    min_element = min(numbers)
    
    # Lock ensures complete output before another thread prints
    with print_lock:
        print("\nThread 2 started")
        print(f"Minimum element: {min_element}")
        print("Thread 2 completed")

def main():
    # Get list of integers from user
    print("Enter numbers separated by spaces:")
    user_input = input()
    numbers = list(map(int, user_input.split()))
    
    print(f"\nInput list: {numbers}")
    
    # Create two threads
    t1 = threading.Thread(target=find_maximum, args=(numbers,), name="Thread1")
    t2 = threading.Thread(target=find_minimum, args=(numbers,), name="Thread2")
    
    # Start both threads
    t1.start()
    t2.start()
    
    # Wait for both threads to complete
    t1.join()
    t2.join()
    
    print("\nBoth threads completed execution")

if __name__ == "__main__":
    main()