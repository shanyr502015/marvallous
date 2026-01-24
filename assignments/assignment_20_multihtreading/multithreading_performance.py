import threading
import time

# Example 1: I/O-Bound Task (File Writing)
def write_file(filename, lines):
    """Simulate I/O operation by writing to file"""
    with open(filename, 'w') as f:
        for i in range(lines):
            f.write(f"Line {i}: This is some sample text for testing\n")
            time.sleep(0.001)  # Simulate slow I/O

def main():
    # Without threading
    start = time.time()
    write_file('file1.txt', 100)
    write_file('file2.txt', 100)
    write_file('file3.txt', 100)
    write_file('file4.txt', 100)
    end = time.time()
    time_without = end - start
    print(f"Without threading: {time_without:.2f} seconds")
    
    # With threading
    start = time.time()
    threads = []
    for i in range(1, 5):
        t = threading.Thread(target=write_file, args=(f'file{i}_threaded.txt', 100))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    end = time.time()
    time_with = end - start
    print(f"With threading: {time_with:.2f} seconds")
   

if __name__ == "__main__":
    main()