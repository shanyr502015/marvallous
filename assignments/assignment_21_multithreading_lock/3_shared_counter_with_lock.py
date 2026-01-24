"""Design a Python application where multiple threads update a shared variable.
• Use a Lock to avoid race conditions.
• Each thread should increment the shared counter multiple times.
• Display the final value of the counter after all threads complete execution."""

import threading
import time

# Shared variable
counter = 0
# Create a lock to avoid race conditions
counter_lock = threading.Lock()

def increment_counter(thread_name, increments):
    """Increment the shared counter multiple times"""
    global counter
    print(f"{thread_name} started")
    
    for i in range(increments):
        # Acquire lock before modifying shared variable
        with counter_lock:
            # Read current value
            temp = counter
            # Simulate some processing time
            time.sleep(0.0001)
            # Increment and write back
            counter = temp + 1
    
    print(f"{thread_name} completed")

def main():
    global counter
    # Get number of threads and increments per thread
    num_threads = int(input("Enter number of threads: "))
    increments_per_thread = int(input("Enter increments per thread: "))
    
    print(f"\nInitial counter value: {counter}")
    print(f"Expected final value: {num_threads * increments_per_thread}\n")
    
    # Create multiple threads
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(
            target=increment_counter, 
            args=(f"Thread-{i+1}", increments_per_thread),
            name=f"Thread-{i+1}"
        )
        threads.append(thread)
    
    # Start all threads
    start_time = time.time()
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    
    # Display results
    print(f"\n{'='*50}")
    print("RESULTS")
    print(f"{'='*50}")
    print(f"Final counter value: {counter}")
    print(f"Expected value: {num_threads * increments_per_thread}")
    print(f"Match: {'✓ YES' if counter == num_threads * increments_per_thread else '✗ NO'}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print(f"{'='*50}")

def demo_without_lock():
    """Demonstration of race condition WITHOUT lock"""
    global counter
    counter = 0
    print("\n" + "="*50)
    print("DEMO: WITHOUT LOCK (Race Condition)")
    print("="*50)
    
    def unsafe_increment(thread_name, increments):
        global counter
        print(f"{thread_name} started")
        for i in range(increments):
            # NO LOCK - Race condition!
            temp = counter
            time.sleep(0.0001)
            counter = temp + 1
        print(f"{thread_name} completed")
    
    threads = []
    num_threads = 5
    increments = 100
    
    for i in range(num_threads):
        thread = threading.Thread(
            target=unsafe_increment,
            args=(f"Thread-{i+1}", increments)
        )
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"\nFinal counter value: {counter}")
    print(f"Expected value: {num_threads * increments}")
    print(f"Data loss: {(num_threads * increments) - counter} increments lost!")
    print("="*50)

if __name__ == "__main__":
    print("🔒 THREAD SYNCHRONIZATION WITH LOCK 🔒\n")
    # Run main program with lock
    main()
    
    # Ask if user wants to see race condition demo
    print("\n\nWould you like to see what happens WITHOUT a lock? (yes/no)")
    response = input().strip().lower()
    
    if response in ['yes', 'y']:
        demo_without_lock()
        print("\n⚠️  Without lock, multiple threads cause RACE CONDITIONS!")
        print("Some increments get lost due to concurrent access.")
        print("This is why we NEED locks for shared variables! ⚠️")


# Features:
# ✅ Shared variable: counter accessed by multiple threads
# ✅ Lock protection: counter_lock prevents race conditions
# ✅ Multiple threads: User-defined number of threads
# ✅ Safe increments: Each thread safely increments the counter
# ✅ Result verification: Shows if final value matches expected value
# ✅ Bonus demo: Shows what happens WITHOUT a lock (race condition)
# with counter_lock:
#     temp = counter      # Read
#     time.sleep(0.0001)  # Simulate processing
#     counter = temp + 1  # Write