# Python Memory Management & Garbage Collection - Complete Guide

Great! Let's add this crucial topic to complete your Python knowledge.

---

## **PART 15: Memory Management in Python**

### **How Python Manages Memory**

Python uses **automatic memory management** - you don't manually allocate/free memory like C/C++.

```
Python Memory Manager
    ├── Private Heap (all Python objects stored here)
    ├── Memory Allocator (manages heap)
    └── Garbage Collector (cleans unused objects)
```

---

## **Key Concept: Everything is an Object**

```python
# In Python, EVERYTHING is an object stored in memory
x = 5           # Integer object
name = "Alice"  # String object
func = print    # Function object
```

**Each object has:**
1. **Type** (int, str, list, etc.)
2. **Value** (the actual data)
3. **Reference count** (how many variables point to it)

---

## **Reference Counting - The Main Mechanism**

### **What is Reference Counting?**

Python tracks **how many references** point to each object.

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # 2 (x + getrefcount's argument)

y = x  # New reference to same list
print(sys.getrefcount(x))  # 3 (x, y, + getrefcount)

del y  # Remove reference
print(sys.getrefcount(x))  # 2 (back to x + getrefcount)
```

### **When Reference Count Reaches 0**

**Object is immediately deleted!**

```python
def example():
    data = [1, 2, 3]  # refcount = 1
    # function ends, refcount = 0
    # List is IMMEDIATELY deallocated

example()  # Memory freed as soon as function exits
```

---

## **Visual Example - Reference Counting**

```python
# Step 1: Create object
a = [1, 2, 3]
# Memory: [1,2,3] ← refcount: 1 (a points to it)

# Step 2: Create another reference
b = a
# Memory: [1,2,3] ← refcount: 2 (a and b point to it)

# Step 3: Remove one reference
del a
# Memory: [1,2,3] ← refcount: 1 (only b points to it)

# Step 4: Remove last reference
del b
# Memory: [1,2,3] ← refcount: 0 → DELETED! ✅
```

---

## **The Problem: Circular References**

### **Reference Counting Fails Here!**

```python
# Circular reference problem
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create circular reference
node1 = Node(1)
node2 = Node(2)

node1.next = node2  # node1 → node2
node2.next = node1  # node2 → node1 (CIRCULAR!)

# Delete references
del node1
del node2

# Problem: Objects still reference each other!
# node1.next → node2 (refcount = 1)
# node2.next → node1 (refcount = 1)
# Neither reaches 0, but both are unreachable! 💥
# This is a MEMORY LEAK with reference counting alone
```

**Visual:**
```
node1 ←→ node2
  ↑       ↑
  └───────┘
Both have refcount=1 but no external references!
Reference counting can't free them!
```

---

## **Garbage Collection - The Solution**

Python has a **Garbage Collector (GC)** that finds and deletes circular references.

### **How GC Works**

1. **Tracks container objects** (lists, dicts, classes, tuples)
2. **Periodically scans** for circular references
3. **Breaks cycles** and frees memory

```python
import gc

# GC runs automatically, but you can control it

# Check if GC is enabled
print(gc.isenabled())  # True

# Disable GC (not recommended!)
gc.disable()

# Enable GC
gc.enable()

# Force garbage collection NOW
gc.collect()  # Returns number of objects collected

# Get GC stats
print(gc.get_count())  # (threshold0, threshold1, threshold2)
print(gc.get_stats())
```

---

## **GC Generations - How It's Optimized**

Python uses **generational garbage collection**.

### **The Three Generations**

```
Generation 0 (Young): New objects
    ↓ Survives collection
Generation 1 (Middle): Survived once
    ↓ Survives collection
Generation 2 (Old): Long-lived objects
```

**Logic:** Most objects die young, so check young objects more often!

```python
import gc

# Get current thresholds
print(gc.get_threshold())  # (700, 10, 10)
# Gen0: collect after 700 allocations
# Gen1: collect after 10 Gen0 collections
# Gen2: collect after 10 Gen1 collections

# Set custom thresholds
gc.set_threshold(1000, 15, 15)
```

---

## **Memory Allocation - The Details**

### **Python's Memory Hierarchy**

```
Operating System Memory
    ↓
Python Memory Manager (pymalloc)
    ↓
Object-specific Allocators
    ↓
Python Objects
```

### **Small Object Optimization (PyMalloc)**

Python optimizes for **small objects** (≤ 512 bytes):

```python
# Small objects use memory pools (fast!)
x = 42          # Uses pool
y = "hello"     # Uses pool
z = [1, 2, 3]   # Uses pool

# Large objects use system malloc
huge_list = [0] * 1_000_000  # System malloc
```

---

## **Object Interning - Memory Optimization**

### **Integer Interning**

Python **reuses** small integers (-5 to 256):

```python
a = 5
b = 5
print(a is b)  # True - Same object in memory!

x = 1000
y = 1000
print(x is y)  # False - Different objects!

# Check memory address
print(id(a))  # Same
print(id(b))  # Same
print(id(x))  # Different
print(id(y))  # Different
```

### **String Interning**

Python automatically interns some strings:

```python
# Identifier-like strings are interned
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True - Same object!

# Non-identifier strings usually aren't
s3 = "hello world!"
s4 = "hello world!"
print(s3 is s4)  # False (might be True in some cases)

# Manual interning
import sys
s5 = sys.intern("hello world!")
s6 = sys.intern("hello world!")
print(s5 is s6)  # True - Forced interning
```

---

## **Memory Leaks in Python**

### **Common Causes**

#### **1. Global Variables**

```python
# MEMORY LEAK - Never freed!
cache = []

def add_data(data):
    cache.append(data)  # Grows forever!

for i in range(1_000_000):
    add_data([i] * 1000)  # Memory keeps growing! 💥
```

**Fix:**
```python
# Use weakref or clear when done
cache = []

def add_data(data):
    cache.append(data)
    if len(cache) > 1000:
        cache.clear()  # Limit size
```

#### **2. Circular References (Without GC)**

```python
import gc
gc.disable()  # Disable GC

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a  # Circular!

del a, b  # Memory leaked! (GC disabled)

gc.enable()  # Re-enable GC
gc.collect()  # Clean up
```

#### **3. Unclosed Files/Connections**

```python
# MEMORY LEAK - File handle not released
def read_file():
    f = open('data.txt')
    data = f.read()
    # Forgot f.close()! Handle leaked!
    return data

# CORRECT
def read_file():
    with open('data.txt') as f:  # Auto-closes
        return f.read()
```

#### **4. Large Objects in Exception Context**

```python
# MEMORY LEAK - Exception keeps reference
def process():
    data = [0] * 10_000_000  # Huge list
    try:
        result = 1 / 0
    except Exception as e:
        # Exception keeps reference to entire stack frame!
        # 'data' stays in memory!
        pass

# FIX
def process():
    data = [0] * 10_000_000
    try:
        result = 1 / 0
    except Exception:  # Don't capture exception
        pass
    finally:
        del data  # Explicitly delete
```

---

## **Memory Profiling Tools**

### **1. sys.getsizeof() - Object Size**

```python
import sys

x = [1, 2, 3]
print(sys.getsizeof(x))  # 88 bytes (on 64-bit Python)

y = [1] * 1000
print(sys.getsizeof(y))  # 8056 bytes

# NOTE: Only shows container size, not contents!
nested = [[1, 2, 3]] * 100
print(sys.getsizeof(nested))  # Only outer list size!
```

### **2. tracemalloc - Memory Tracking**

```python
import tracemalloc

# Start tracking
tracemalloc.start()

# Your code here
data = [i for i in range(1_000_000)]

# Get current memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")

# Get top memory consumers
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("\n[ Top 3 memory users ]")
for stat in top_stats[:3]:
    print(stat)

# Stop tracking
tracemalloc.stop()
```

### **3. memory_profiler - Line-by-Line**

```python
# Install: pip install memory_profiler

from memory_profiler import profile

@profile
def my_function():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

my_function()

# Output shows memory usage per line:
# Line #    Mem usage    Increment
#      2     38.8 MiB     38.8 MiB   @profile
#      3     46.5 MiB      7.7 MiB   a = [1] * (10 ** 6)
#      4    199.1 MiB    152.6 MiB   b = [2] * (2 * 10 ** 7)
#      5     46.6 MiB   -152.5 MiB   del b
```

### **4. objgraph - Find Memory Leaks**

```python
# Install: pip install objgraph

import objgraph

# Show most common object types
objgraph.show_most_common_types()

# Track object growth
objgraph.show_growth()

# ... run your code ...

objgraph.show_growth()  # See what increased

# Find all references to an object
x = [1, 2, 3]
objgraph.show_refs([x], filename='refs.png')

# Find what's keeping object alive
objgraph.show_backrefs([x], filename='backrefs.png')
```

---

## **`__del__` Method - Destructor**

### **When Object is Deleted**

```python
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")
    
    def __del__(self):
        print(f"{self.name} destroyed")

obj = MyClass("Object1")
# Output: Object1 created

del obj
# Output: Object1 destroyed (immediately!)
```

### **⚠️ Warning: Don't Rely on `__del__`!**

```python
# PROBLEM: Circular reference delays __del__
class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None
    
    def __del__(self):
        print(f"{self.name} destroyed")

a = Node("A")
b = Node("B")
a.ref = b
b.ref = a  # Circular!

del a, b
# __del__ might not be called immediately!
# Waits for GC to break cycle

import gc
gc.collect()  # Now __del__ is called
```

---

## **Weak References - Avoiding Cycles**

### **Problem with Strong References**

```python
class Cache:
    def __init__(self):
        self.data = {}
    
    def add(self, key, obj):
        self.data[key] = obj  # Strong reference!
        # Object can't be garbage collected!

cache = Cache()
obj = [1, 2, 3]
cache.add('mydata', obj)

del obj  # Object still in cache! Not freed!
```

### **Solution: Weak References**

```python
import weakref

class Cache:
    def __init__(self):
        self.data = {}
    
    def add(self, key, obj):
        self.data[key] = weakref.ref(obj)  # Weak reference!
    
    def get(self, key):
        ref = self.data.get(key)
        return ref() if ref else None  # Dereference

cache = Cache()
obj = [1, 2, 3]
cache.add('mydata', obj)

print(cache.get('mydata'))  # [1, 2, 3]

del obj  # Object can be freed now!
print(cache.get('mydata'))  # None (object was collected)
```

### **WeakValueDictionary - Built-in Weak Cache**

```python
import weakref

# Automatically removes entries when object dies
cache = weakref.WeakValueDictionary()

obj = [1, 2, 3]
cache['mydata'] = obj

print(cache['mydata'])  # [1, 2, 3]

del obj  # Object freed
print(cache.get('mydata'))  # None (auto-removed!)
```

---

## **Memory Management Best Practices**

### **1. Use Context Managers**

```python
# BAD - Manual cleanup
f = open('file.txt')
data = f.read()
f.close()  # Might forget!

# GOOD - Automatic cleanup
with open('file.txt') as f:
    data = f.read()
# File automatically closed
```

### **2. Limit Global Variables**

```python
# BAD - Global cache grows forever
cache = {}

def get_data(key):
    if key not in cache:
        cache[key] = expensive_operation(key)
    return cache[key]

# GOOD - Use LRU cache with size limit
from functools import lru_cache

@lru_cache(maxsize=128)  # Only keeps 128 items
def get_data(key):
    return expensive_operation(key)
```

### **3. Delete Large Objects When Done**

```python
def process_data():
    # Load huge dataset
    data = load_huge_file()  # 1GB
    
    # Process it
    result = analyze(data)
    
    # Free memory immediately
    del data  # Don't wait for function to end
    
    return result
```

### **4. Use Generators for Large Sequences**

```python
# BAD - Loads everything in memory
def get_numbers():
    return [i for i in range(1_000_000)]  # ~8MB

data = get_numbers()

# GOOD - Generates on demand
def get_numbers():
    return (i for i in range(1_000_000))  # ~200 bytes

data = get_numbers()
```

### **5. Be Careful with Closures**

```python
# BAD - Closure keeps reference to huge_data
def create_processor(huge_data):
    def process(x):
        # Even though we don't use huge_data,
        # it's kept alive by closure!
        return x * 2
    return process

# GOOD - Don't capture unnecessary variables
def create_processor():
    def process(x):
        return x * 2
    return process
```

---

## **Slots - Memory Optimization**

### **Normal Class**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
import sys
print(sys.getsizeof(p.__dict__))  # ~240 bytes (dict overhead!)
```

### **With `__slots__`**

```python
class Point:
    __slots__ = ['x', 'y']  # Fixed attributes
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
# No __dict__! Direct attribute storage
print(sys.getsizeof(p))  # ~64 bytes (much smaller!)

# Can't add new attributes
p.z = 3  # AttributeError! ❌
```

**Memory Savings:**
```python
# Create 1 million points

# Without slots
points = [Point(i, i) for i in range(1_000_000)]
# ~240 MB

# With slots
points = [Point(i, i) for i in range(1_000_000)]
# ~64 MB (saves 176 MB!)
```

---

## **Understanding Memory in Collections**

### **List Pre-allocation**

```python
import sys

lst = []
print(sys.getsizeof(lst))  # 56 bytes (empty)

lst.append(1)
print(sys.getsizeof(lst))  # 88 bytes (room for 4 items!)

for i in range(2, 10):
    lst.append(i)
print(sys.getsizeof(lst))  # 152 bytes (room for 13 items)

# Lists over-allocate to avoid frequent resizing
```

### **Dictionary Memory**

```python
d = {}
print(sys.getsizeof(d))  # 232 bytes (empty)

# Dictionaries are sparse (memory for hash table)
d['a'] = 1
print(sys.getsizeof(d))  # 232 bytes (still same)

# More items
for i in range(100):
    d[i] = i
print(sys.getsizeof(d))  # 4696 bytes
```

### **Set vs List Memory**

```python
data = list(range(1000))
print(sys.getsizeof(data))  # 8856 bytes

data_set = set(range(1000))
print(sys.getsizeof(data_set))  # 32992 bytes

# Sets use more memory (hash table)
# But O(1) lookup vs O(n) for lists
```

---

## **Complete Memory Management Checklist**

### **Understanding**
□ Know reference counting is the primary mechanism  
□ Understand garbage collection handles circular references  
□ Know about generational GC (3 generations)  
□ Understand object interning for small ints and strings  

### **Debugging**
□ Use `sys.getsizeof()` for object size  
□ Use `tracemalloc` for memory tracking  
□ Use `gc.get_objects()` to find memory leaks  
□ Use `weakref` to avoid keeping objects alive  

### **Optimization**
□ Use `__slots__` for classes with many instances  
□ Use generators instead of lists for large sequences  
□ Use `with` statements for resource management  
□ Delete large objects when done (`del`)  
□ Use `@lru_cache` with `maxsize` for caching  

### **Avoiding Leaks**
□ Close files/connections (use `with`)  
□ Avoid circular references or use `weakref`  
□ Limit global variable growth  
□ Be careful with exception contexts  
□ Don't rely on `__del__` for cleanup  

---

## **Interview Questions - Memory Management**

**Q: How does Python manage memory?**
> Python uses automatic memory management with reference counting as the primary mechanism and a garbage collector for circular references. All objects are stored in a private heap managed by Python's memory manager.

**Q: What is reference counting?**
> Each object tracks how many references point to it. When the count reaches zero, the object is immediately deallocated. However, reference counting can't handle circular references.

**Q: What is garbage collection in Python?**
> A supplementary mechanism that finds and collects objects involved in circular references. It uses generational collection with 3 generations, checking younger objects more frequently.

**Q: When does GC run?**
> Automatically when allocation thresholds are reached (default: 700 objects in gen0, 10 collections for gen1, 10 for gen2). Can also be triggered manually with `gc.collect()`.

**Q: What are memory leaks in Python?**
> Unintended retention of objects that should be freed. Common causes: global variables that grow indefinitely, circular references with GC disabled, unclosed resources, and exception contexts keeping large objects alive.

**Q: What is `__slots__`?**
> A class attribute that restricts instance attributes to a fixed set, eliminating the `__dict__` overhead and saving memory. Useful for classes with many instances.

**Q: What is weak reference?**
> A reference that doesn't prevent an object from being garbage collected. Useful for caches where you don't want to keep objects alive just because they're cached.

**Q: Difference between `==` and `is`?**
> `==` compares values (equality), `is` compares identity (same object in memory). Due to interning, `is` works for small integers and some strings but shouldn't be relied upon.

---

## **Quick Reference - Memory Commands**

```python
import sys
import gc
import tracemalloc
import weakref

# Object size
sys.getsizeof(obj)

# Reference count
sys.getrefcount(obj)

# Force garbage collection
gc.collect()

# Get all objects
gc.get_objects()

# Track memory
tracemalloc.start()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Weak reference
weak_obj = weakref.ref(obj)
weak_obj()  # Dereference (returns obj or None)

# Weak dictionary
cache = weakref.WeakValueDictionary()
```