'''Design a Python application that creates three threads named Small, Capital, and Digits.
• All threads should accept a string as input.
• The Small thread should count and display the number of lowercase characters.
• The Capital thread should count and display the number of uppercase characters.
• The Digits thread should count and display the number of numeric digits.
• Each thread must also display:
        o Thread ID
        o Thread Name'''

import threading

# def Small(text):
#     """Count and display number of lowercase characters"""
#     thread_id = threading.get_ident()
#     thread_name = threading.current_thread().name
    
#     count = sum(1 for char in text if char.islower())
    
#     print(f"\nThread Name: {thread_name}")
#     print(f"Number of lowercase characters: {count}")
#     print(f"Thread ID: {thread_id}")

# def Capital(text):
#     """Count and display number of uppercase characters"""
#     thread_id = threading.get_ident()
#     thread_name = threading.current_thread().name
    
#     count = sum(1 for char in text if char.isupper())
    
#     print(f"\nThread Name: {thread_name}")
#     print(f"Number of uppercase characters: {count}")
#     print(f"Thread ID: {thread_id}")

# def Digits(text):
#     """Count and display number of numeric digits"""
#     thread_id = threading.get_ident()
#     thread_name = threading.current_thread().name
    
#     count = sum(1 for char in text if char.isdigit())
    
#     print(f"\nThread Name: {thread_name}")
#     print(f"Number of numeric digits: {count}")
#     print(f"Thread ID: {thread_id}")

# def main():
#     # Get string input from user
#     text = input("Enter a string: ")
    
#     print(f"\nInput string: {text}")
    
#     # Create three threads
#     t1 = threading.Thread(target=Small, args=(text,), name="Small")
#     t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
#     t3 = threading.Thread(target=Digits, args=(text,), name="Digits")
    
#     # Start all threads
#     t1.start()
#     t2.start()
#     t3.start()
    
#     # Wait for all threads to complete
#     t1.join()
#     t2.join()
#     t3.join()
    
#     print("\nAll threads completed execution")

# if __name__ == "__main__":
#     main()

 ########### WITH LOCK SYSNCRONIZATION ############


# Create a lock for synchronized printing
print_lock = threading.Lock()

def Small(text):
    """Count and display number of lowercase characters"""
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    
    count = sum(1 for char in text if char.islower())
    
    # Lock ensures complete output before another thread prints
    with print_lock:
        print(f"\nThread Name: {thread_name}")
        print(f"Number of lowercase characters: {count}")
        print(f"Thread ID: {thread_id}")

def Capital(text):
    """Count and display number of uppercase characters"""
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    
    count = sum(1 for char in text if char.isupper())
    
    # Lock ensures complete output before another thread prints
    with print_lock:
        print(f"\nThread Name: {thread_name}")
        print(f"Number of uppercase characters: {count}")
        print(f"Thread ID: {thread_id}")

def Digits(text):
    """Count and display number of numeric digits"""
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    
    count = sum(1 for char in text if char.isdigit())
    
    # Lock ensures complete output before another thread prints
    with print_lock:
        print(f"\nThread Name: {thread_name}")
        print(f"Number of numeric digits: {count}")
        print(f"Thread ID: {thread_id}")

def main():
    # Get string input from user
    text = input("Enter a string: ")
    
    print(f"\nInput string: {text}")
    
    # Create three threads
    t1 = threading.Thread(target=Small, args=(text,), name="Small")
    t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(text,), name="Digits")
    
    # Start all threads
    t1.start()
    t2.start()
    t3.start()
    
    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()
    
    print("\nAll threads completed execution")

if __name__ == "__main__":
    main()