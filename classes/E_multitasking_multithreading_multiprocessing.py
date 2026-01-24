# Complete Python Concurrency & Memory 

####################### PART 1: Multithreading vs Multiprocessing Basics #######################
################################################################################################

### *Core Concept*
- Multithreading: Multiple threads, one process, **shared memory**
- Multiprocessing: Multiple processes, **separate memory**

### The Golden Rule**
I/O-bound → Use Threading
CPU-bound → Use Multiprocessing

### Memory Trick
🧵 Threading = Talking to servers (I/O)  
⚙️ Multiprocessing = Math & Muscle work (CPU)

### **Quick Comparison**

| Feature | Threading | Multiprocessing |
|---------|-----------|-----------------|
| **Memory** | Shared | Separate (copied) |
| **Speed to Start** | Fast (lightweight) | Slow (heavy) |
| **True Parallelism** | ❌ No (GIL blocks) | ✅ Yes |
| **Best For** | I/O-bound | CPU-bound |
| **Communication** | Easy (shared vars) | Hard (Queue, Pipe) |
| **GIL Impact** | Limited by GIL | No GIL (each has own) |

---

## **PART 2: The GIL (Global Interpreter Lock) - CRITICAL!**

### **What is GIL?**
A lock that allows only **ONE thread** to execute Python code at a time.

### **Why GIL Exists**
- **Memory safety** in CPython
- Makes single-threaded programs faster
- Simplifies C extension development

### **GIL's Impact**

```python
# CPU-bound with threading (GIL ruins it)
Thread 1: [COMPUTE][wait-GIL][COMPUTE][wait-GIL]
Thread 2: [wait-GIL][COMPUTE][wait-GIL][COMPUTE]
Result: NO speedup, fighting for GIL

# I/O-bound with threading (GIL doesn't matter!)
Thread 1: [START-REQUEST]...(waiting - GIL released)...[PROCESS]
Thread 2: [START-REQUEST]...(waiting - GIL released)...[PROCESS]
Thread 3: [START-REQUEST]...(waiting - GIL released)...[PROCESS]
Result: BIG speedup, concurrent waiting!
```

### **Key Insight: When GIL is Released**
✅ During I/O operations (network, file, database)  
✅ During `time.sleep()`  
✅ During blocking system calls  
❌ NOT during CPU computation

---

## **PART 3: Why Python Has BOTH Threading and GIL**

### **The Apparent Contradiction**
"If GIL prevents parallel execution, why have threading?"

### **The Answer**
Threading ≠ Parallelism  
Threading = **Concurrency** (overlapping tasks)

### **Real Example - Web Scraping**

```python
import threading
import requests
import time

urls = ['url1', 'url2', 'url3', 'url4', 'url5']

def fetch(url):
    response = requests.get(url)  # ← Waiting here (GIL RELEASED!)
    return len(response.text)

# WITHOUT threading
start = time.time()
for url in urls:
    fetch(url)  # 5 URLs × 2 sec each = 10 seconds
print(f"Sequential: {time.time() - start}s")  # ~10 seconds

# WITH threading
start = time.time()
threads = [threading.Thread(target=fetch, args=(url,)) for url in urls]
for t in threads: t.start()
for t in threads: t.join()
print(f"Threaded: {time.time() - start}s")  # ~2 seconds!
```

**Why it works**: All threads wait for I/O simultaneously!

---

## **PART 4: Basic Code Patterns**

### **Threading Pattern**

```python
from threading import Thread

def worker(name):
    print(f"Thread {name} working...")

# Create and start
threads = []
for i in range(5):
    t = Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all to finish
for t in threads:
    t.join()

print("All done!")
```

### **Multiprocessing Pattern**

```python
from multiprocessing import Process

def worker(name):
    print(f"Process {name} working...")

# Create and start
processes = []
for i in range(5):
    p = Process(target=worker, args=(i,))
    processes.append(p)
    p.start()

# Wait for all to finish
for p in processes:
    p.join()

print("All done!")
```

### **Modern Way - ThreadPoolExecutor**

```python
from concurrent.futures import ThreadPoolExecutor

def download(url):
    # download logic
    return result

urls = ['url1', 'url2', 'url3']

# Automatic thread management
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(download, urls)
    
for result in results:
    print(result)
```

### **Modern Way - ProcessPoolExecutor**

```python
from concurrent.futures import ProcessPoolExecutor
import os

def heavy_computation(data):
    # CPU intensive work
    return result

data_list = [1, 2, 3, 4, 5]

# Use cpu_count() for optimal workers
with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    results = executor.map(heavy_computation, data_list)
    
for result in results:
    print(result)
```

---

## **PART 5: Lock Synchronization - CRITICAL CONCEPT**

### **The Big Question**
"Do we need locks if GIL exists?"

**Answer: YES! Absolutely!**

### **GIL vs Lock - The Difference**

| Feature | GIL | Lock |
|---------|-----|------|
| **Controls** | Python interpreter | Your specific resource |
| **Scope** | All Python bytecode | Code you choose |
| **Protects** | Python internals | Your shared data |
| **You control?** | ❌ No (automatic) | ✅ Yes (manual) |

**Analogy:**
- **GIL** = Building security (protects structure)
- **Lock** = Your apartment door (protects YOUR stuff)

### **Why Locks Are Needed - The Race Condition**

```python
# WITHOUT LOCK - BROKEN!
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # NOT atomic!

t1 = Thread(target=increment)
t2 = Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()

print(counter)  # Expected: 200,000
                # Actual: ~150,000 (WRONG!) 😱
```

### **What Happens Under the Hood**

```python
# counter += 1 is actually THREE operations:
temp = counter      # 1. Read
temp = temp + 1     # 2. Add
counter = temp      # 3. Write

# The Race:
Thread 1: Read counter (0)
Thread 2: Read counter (0)  ← Both read 0!
Thread 1: Add 1 → 1
Thread 2: Add 1 → 1
Thread 1: Write 1
Thread 2: Write 1  ← Overwrites! Lost increment!
# Result: 1 instead of 2
```

### **Solution: Use Lock**

```python
from threading import Lock

counter = 0
lock = Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # ← Only ONE thread at a time!
            counter += 1

t1 = Thread(target=increment)
t2 = Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()

print(counter)  # Always: 200,000 ✅
```

### **Real-World Example - Bank Account**

```python
# DANGEROUS - WITHOUT LOCK
class BankAccount:
    def __init__(self):
        self.balance = 1000
    
    def withdraw(self, amount):
        if self.balance >= amount:
            # ⚠️ Thread switch can happen here!
            self.balance -= amount
            return True
        return False

# Two threads withdraw 800 each
# Both check balance (1000 >= 800) → True
# Both withdraw → Balance = -600! 💥
```

```python
# SAFE - WITH LOCK
from threading import Lock

class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = Lock()
    
    def withdraw(self, amount):
        with self.lock:  # ← Atomic operation!
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False

# Now only one withdrawal at a time ✅
# Second thread waits, sees insufficient balance
```

---

## **PART 6: When to Use Locks**

### **NEED Locks ✅**

```python
# 1. Modifying shared variables
shared_list.append(item)      # Need lock!
shared_dict[key] = value      # Need lock!
counter += 1                  # Need lock!

# 2. Multiple operations together
if account.balance >= amount:
    account.balance -= amount  # Need lock for BOTH!

# 3. Non-atomic operations
balance = balance - 100       # Need lock!
```

### **DON'T Need Locks ❌**

```python
# 1. Read-only operations
value = shared_list[0]        # Just reading, OK

# 2. Thread-local data
from threading import local
thread_data = local()
thread_data.value = 10        # Each thread separate, OK

# 3. Thread-safe structures
from queue import Queue
q = Queue()
q.put(item)                   # Already thread-safe!
q.get()                       # Already thread-safe!
```

---

## **PART 7: Types of Locks**

### **1. Basic Lock**
```python
from threading import Lock

lock = Lock()

with lock:
    # Critical section
    shared_resource += 1
```

### **2. RLock (Reentrant Lock)**
```python
from threading import RLock

rlock = RLock()

def recursive_function():
    with rlock:
        # Can acquire same lock multiple times
        with rlock:  # ✅ Works! (Lock would deadlock)
            # Nested critical section
            pass
```

### **3. Semaphore**
```python
from threading import Semaphore

# Allow max 3 threads simultaneously
sem = Semaphore(3)

def access_resource():
    with sem:
        # Only 3 threads can be here at once
        print("Accessing limited resource")
```

### **4. Event**
```python
from threading import Event

event = Event()

def waiter():
    print("Waiting for event...")
    event.wait()  # Block until set
    print("Event received!")

def setter():
    time.sleep(2)
    event.set()  # Wake up all waiters
```

---

## **PART 8: Inter-Process Communication**

### **Problem**
Processes have **separate memory**, can't share variables directly.

### **Solutions**

#### **1. Queue (Most Common)**
```python
from multiprocessing import Process, Queue

def producer(q):
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")

q = Queue()
p1 = Process(target=producer, args=(q,))
p2 = Process(target=consumer, args=(q,))

p1.start(); p2.start()
p1.join()
q.put(None)  # Signal to stop
p2.join()
```

#### **2. Pipe**
```python
from multiprocessing import Process, Pipe

def sender(conn):
    conn.send("Hello from process!")
    conn.close()

def receiver(conn):
    msg = conn.recv()
    print(msg)

parent_conn, child_conn = Pipe()
p1 = Process(target=sender, args=(child_conn,))
p2 = Process(target=receiver, args=(parent_conn,))

p1.start(); p2.start()
p1.join(); p2.join()
```

#### **3. Shared Memory (Advanced)**
```python
from multiprocessing import Process, Value, Array

def increment(shared_val, shared_arr):
    shared_val.value += 1
    for i in range(len(shared_arr)):
        shared_arr[i] *= 2

# 'i' = integer, 'd' = double
shared_num = Value('i', 0)
shared_array = Array('i', [1, 2, 3, 4, 5])

p = Process(target=increment, args=(shared_num, shared_array))
p.start()
p.join()

print(shared_num.value)      # 1
print(shared_array[:])       # [2, 4, 6, 8, 10]
```

---

## **PART 9: Common Patterns & Best Practices**

### **Pattern 1: Thread Pool for Multiple URLs**

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    response = requests.get(url)
    return len(response.content)

urls = ['http://example.com'] * 10

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_url, urls))

print(f"Total bytes: {sum(results)}")
```

### **Pattern 2: Process Pool for Data Processing**

```python
from concurrent.futures import ProcessPoolExecutor
import os

def process_data(chunk):
    # Heavy CPU work
    return sum(x**2 for x in chunk)

data = [list(range(1000000)) for _ in range(10)]

with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    results = list(executor.map(process_data, data))

print(f"Total: {sum(results)}")
```

### **Pattern 3: Producer-Consumer with Queue**

```python
from threading import Thread
from queue import Queue
import time

def producer(q):
    for i in range(10):
        time.sleep(0.1)
        q.put(i)
        print(f"Produced: {i}")
    q.put(None)  # Sentinel value

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        q.task_done()

q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))

t1.start(); t2.start()
t1.join(); t2.join()
```

### **Pattern 4: Daemon Threads**

```python
from threading import Thread
import time

def background_task():
    while True:
        print("Background running...")
        time.sleep(1)

# Daemon dies when main program exits
t = Thread(target=background_task, daemon=True)
t.start()

time.sleep(3)
print("Main exiting, daemon will die")
# No need to join daemon threads
```

---

## **PART 10: Interview Quick Reference**

### **Must-Know Questions & Answers**

**Q: Threading vs Multiprocessing?**
> Threading for I/O-bound (network, files), Multiprocessing for CPU-bound (calculations). Reason: GIL prevents true parallelism in threads.

**Q: What is GIL?**
> Global Interpreter Lock - allows only one thread to execute Python code at a time. Protects memory but limits CPU parallelism.

**Q: Do we need locks with GIL?**
> Yes! GIL protects Python internals, not our data. Operations like `counter += 1` aren't atomic and need locks to prevent race conditions.

**Q: How many processes to create?**
> Usually `os.cpu_count()` for CPU-bound tasks. More processes than cores causes overhead.

**Q: What's a race condition?**
> When multiple threads access shared data simultaneously, causing unpredictable results. Fix with locks.

**Q: Daemon thread vs normal thread?**
> Daemon threads run in background and terminate when main program exits. Normal threads keep program alive.

**Q: How to share data between processes?**
> Use Queue, Pipe, Manager, or shared memory (Value, Array). Processes can't share variables directly.

---

## **PART 11: Complete Working Examples**

### **Example 1: I/O-Bound - Download Multiple Files**

```python
from concurrent.futures import ThreadPoolExecutor
import requests
import time

def download_file(url):
    print(f"Downloading {url}...")
    response = requests.get(url)
    print(f"Finished {url}: {len(response.content)} bytes")
    return len(response.content)

urls = [
    'http://example.com',
    'http://example.org',
    'http://example.net',
] * 3

# Sequential
start = time.time()
for url in urls:
    download_file(url)
print(f"Sequential: {time.time() - start:.2f}s")

# Threaded
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(download_file, urls))
print(f"Threaded: {time.time() - start:.2f}s")
print(f"Total downloaded: {sum(results)} bytes")
```

### **Example 2: CPU-Bound - Calculate Prime Numbers**

```python
from concurrent.futures import ProcessPoolExecutor
import time
import os

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(range_start, range_end):
    count = sum(1 for n in range(range_start, range_end) if is_prime(n))
    return count

ranges = [(i, i+10000) for i in range(0, 100000, 10000)]

# Sequential
start = time.time()
total = sum(count_primes(s, e) for s, e in ranges)
print(f"Sequential: {time.time() - start:.2f}s, Primes: {total}")

# Multiprocessing
start = time.time()
with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    results = executor.map(lambda r: count_primes(r[0], r[1]), ranges)
    total = sum(results)
print(f"Multiprocessing: {time.time() - start:.2f}s, Primes: {total}")
```

### **Example 3: Thread-Safe Counter**

```python
from threading import Thread, Lock
import time

class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()
    
    def increment(self):
        with self.lock:
            temp = self.count
            time.sleep(0.0001)  # Simulate some work
            self.count = temp + 1

# Test it
counter = SafeCounter()
threads = [Thread(target=counter.increment) for _ in range(100)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Final count: {counter.count}")  # Always 100 ✅
```

---

## **PART 12: Debugging & Common Mistakes**

### **Mistake 1: Forgetting join()**
```python
# WRONG - Main exits before threads finish
t = Thread(target=worker)
t.start()
# Program might exit before thread completes!

# CORRECT
t = Thread(target=worker)
t.start()
t.join()  # Wait for completion
```

### **Mistake 2: Sharing Mutable Objects Without Locks**
```python
# WRONG
shared_list = []

def add_items():
    for i in range(1000):
        shared_list.append(i)  # Race condition!

# CORRECT
from threading import Lock
shared_list = []
lock = Lock()

def add_items():
    for i in range(1000):
        with lock:
            shared_list.append(i)
```

### **Mistake 3: Using Threading for CPU-bound**
```python
# WRONG - No speedup due to GIL
def calculate(n):
    return sum(i**2 for i in range(n))

with ThreadPoolExecutor() as executor:
    results = executor.map(calculate, [1000000] * 10)

# CORRECT - Use multiprocessing
with ProcessPoolExecutor() as executor:
    results = executor.map(calculate, [1000000] * 10)
```

### **Mistake 4: Deadlock**
```python
# WRONG - Can deadlock
lock1 = Lock()
lock2 = Lock()

def thread1():
    with lock1:
        with lock2:  # If thread2 has lock2, deadlock!
            pass

def thread2():
    with lock2:
        with lock1:  # If thread1 has lock1, deadlock!
            pass

# CORRECT - Always acquire locks in same order
def thread1():
    with lock1:
        with lock2:
            pass

def thread2():
    with lock1:  # Same order!
        with lock2:
            pass
```

---

## **PART 13: Memory Summary**

### **The Complete Mental Model**

```
Task Type?
    │
    ├─ I/O-bound (waiting for network/disk/database)
    │   └─► Use THREADING
    │       • GIL released during I/O
    │       • Concurrent waiting = speedup
    │       • Shared memory (easy)
    │       • Need locks for shared data!
    │
    └─ CPU-bound (calculations/processing)
        └─► Use MULTIPROCESSING
            • Bypasses GIL
            • True parallel execution
            • Separate memory (harder)
            • Use Queue/Pipe to communicate
```

### **Key Takeaways**
1. **GIL** limits threads but NOT processes
2. **Threading** works for I/O despite GIL (releases during wait)
3. **Locks** protect YOUR data, GIL protects Python
4. **ThreadPoolExecutor/ProcessPoolExecutor** = modern, clean way
5. **Queue** = best way for inter-process communication

---

## Quick Revision Checklist**

□ Know when to use threading vs multiprocessing  
□ Understand what GIL is and why it exists  
□ Know why threading still works for I/O  
□ Understand race conditions  
□ Know when locks are needed  
□ Understand GIL ≠ Lock protection  
□ Know how to use ThreadPoolExecutor  
□ Know how to use ProcessPoolExecutor  
□ Understand inter-process communication (Queue, Pipe)  
□ Know common mistakes (deadlock, forgetting join, no locks)  

