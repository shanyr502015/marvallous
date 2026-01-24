import threading
import time

def display_even():
    for i in range(1, 11):
        even_number = i * 2
        print(f"Even: {even_number}")
    # print("Even thread completed")
    print("Even completed")

def display_odd():
    for i in range(10):
        odd_number = 2 * i + 1
        print(f"Odd: {odd_number}")
    # print("Odd thread completed")
    print("Odd completed")

def main():
    # start_time = time.time()
    # # Create two threads
    # even_thread = threading.Thread(target=display_even, name="Even")
    # odd_thread = threading.Thread(target=display_odd, name="Odd")
    # # Start both threads
    # even_thread.start()
    # odd_thread.start()
    # # Wait for both threads to complete
    # even_thread.join()
    # odd_thread.join()
    # end_time = time.time()
    # print("time required with threading:", end_time - start_time) # 0.003997802734375

    start_time = time.time()
    display_even()
    display_odd()
    end_time = time.time()
    print("time required without threading :",start_time-end_time) # -0.002687692642211914
    
if __name__ == "__main__":
    main()


# Correct Interpretation
# The negative value doesn't mean it's faster - it just means you subtracted in the wrong order!

# -0.0027 seconds means the calculation is backwards
# The actual time taken is +0.0027 seconds (2.7 milliseconds)

# Comparison

# With threading: 0.004 seconds (4 milliseconds)
# Without threading: 0.0027 seconds (2.7 milliseconds) - after fixing the calculation

# Why is Threading "Slower" Here?
# For such a simple task (just printing 20 numbers), threading actually adds overhead:

# Thread creation overhead - Creating threads takes time
# Context switching - OS switches between threads
# GIL (Global Interpreter Lock) - Python's GIL prevents true parallel execution for CPU-bound tasks

# Threading is beneficial when:

# You have I/O operations (file reading, network requests, database queries)
# You have long-running tasks
# You need responsiveness (GUI applications)

# For this tiny task, the overhead of creating threads exceeds any benefit. But the requirement was to demonstrate threading, not necessarily to improve performance!
# Fix your subtraction and you'll see both take similar (very small) amounts of time.