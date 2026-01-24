import threading

def Thread1():
    """Display numbers from 1 to 50"""
    print("\nThread1 started")
    print("Numbers from 1 to 50:")
    for i in range(1, 51):
        print(i, end=" ")
    print("\nThread1 completed\n")

def Thread2():
    """Display numbers from 50 to 1 in reverse order"""
    print("Thread2 started")
    print("Numbers from 50 to 1:")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("\nThread2 completed")

def main():
    # Create two threads
    t1 = threading.Thread(target=Thread1, name="Thread1")
    t2 = threading.Thread(target=Thread2, name="Thread2")
    
    # Start Thread1
    t1.start()
    # Wait for Thread1 to complete before starting Thread2
    t1.join()
    
    # Start Thread2 only after Thread1 has completed
    t2.start()
    # Wait for Thread2 to complete
    t2.join()
    
    print("\n\nBoth threads completed execution")

if __name__ == "__main__":
    main()