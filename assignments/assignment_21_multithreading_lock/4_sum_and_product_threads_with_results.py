import threading

# Dictionary to store results from threads
results = {}

# Create a lock for synchronized access to results
result_lock = threading.Lock()

def compute_sum(numbers, thread_name):
    """Compute the sum of elements from the list"""
    print(f"\n{thread_name} started")
    
    total_sum = sum(numbers)
    
    # Store result safely
    with result_lock:
        results['sum'] = total_sum
    
    print(f"{thread_name} completed - Sum calculated: {total_sum}")

def compute_product(numbers, thread_name):
    """Compute the product of elements from the list"""
    print(f"\n{thread_name} started")
    
    product = 1
    for num in numbers:
        product *= num
    
    # Store result safely
    with result_lock:
        results['product'] = product
    
    print(f"{thread_name} completed - Product calculated: {product}")

def main():
    # Get list of numbers from user
    print("Enter numbers separated by spaces:")
    user_input = input()
    numbers = list(map(int, user_input.split()))
    
    print(f"\nInput list: {numbers}")
    
    # Create two threads
    t1 = threading.Thread(target=compute_sum, args=(numbers, "Thread-1"), name="Thread-1")
    t2 = threading.Thread(target=compute_product, args=(numbers, "Thread-2"), name="Thread-2")
    
    # Start both threads
    t1.start()
    t2.start()
    
    # Wait for both threads to complete
    t1.join()
    t2.join()
    
    # Display results from main thread
    print("\n" + "="*50)
    print("RESULTS FROM MAIN THREAD")
    print("="*50)
    print(f"Sum of elements: {results.get('sum', 'Not calculated')}")
    print(f"Product of elements: {results.get('product', 'Not calculated')}")
    print("="*50)
    
    print("\nBoth threads completed execution")

if __name__ == "__main__":
    main()


# EXAMPLE OUTPUT
# Enter numbers separated by spaces:
# 2 3 4 5 6

# Input list: [2, 3, 4, 5, 6]

# Thread-1 started
# Thread-1 completed - Sum calculated: 20

# Thread-2 started
# Thread-2 completed - Product calculated: 720

# ==================================================
# RESULTS FROM MAIN THREAD
# ==================================================
# Sum of elements: 20
# Product of elements: 720
# ==================================================

# Both threads completed execution

# Features:
# ✅ Thread 1: Computes the sum of all elements
# ✅ Thread 2: Computes the product of all elements
# ✅ Shared results dictionary: Stores results from both threads
# ✅ Thread-safe storage: Uses lock to safely store results
# ✅ Main thread retrieval: Main thread displays results after threads complete
# ✅ Concurrent execution: Both calculations happen simultaneously

# How Results Are Returned:
# Threads store results in shared dictionary
# results = {}

# # Thread 1 stores sum
# with result_lock:
#     results['sum'] = total_sum

# # Thread 2 stores product
# with result_lock:
#     results['product'] = product

# # Main thread retrieves results
# print(f"Sum: {results['sum']}")
# print(f"Product: {results['product']}")

# Try These Examples:
# 1 2 3 4 5 → Sum: 15, Product: 120
# 10 20 30 → Sum: 60, Product: 6000
# 2 2 2 2 2 → Sum: 10, Product: 32
# 5 10 15 20 → Sum: 50, Product: 15000