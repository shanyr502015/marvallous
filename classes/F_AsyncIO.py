# AsyncIO - The Third Way of Concurrency in Python

You're right! AsyncIO is a **crucial** third option. Let me add it to your notes.

---

## **PART 14: AsyncIO - Async/Await**

### **The Three Ways of Concurrency**

```
1. Threading    → I/O-bound (OS-level concurrency)
2. Multiprocessing → CPU-bound (true parallelism)
3. AsyncIO      → I/O-bound (single-threaded concurrency)
```

### **What is AsyncIO?**

**Cooperative multitasking** on a **single thread** using `async`/`await`.

**Key Concept**: One thread voluntarily yields control during I/O waits.

---

## **AsyncIO vs Threading - The Big Difference**

### **Threading (Preemptive)**
```
OS decides when to switch threads (preemptive)
Thread 1: [work][work][SWITCH][work]
Thread 2: [wait][SWITCH][work][work]
          ↑ OS interrupts
```

### **AsyncIO (Cooperative)**
```
Code decides when to yield (cooperative)
Task 1: [work][await][yield control][work]
Task 2: [wait][await][yield control][work]
        ↑ Programmer controls
```

---

## **When to Use What - Complete Guide**

| Scenario | Best Choice | Why |
|----------|-------------|-----|
| **Web scraping** | AsyncIO or Threading | Both work, AsyncIO more efficient |
| **Heavy calculations** | Multiprocessing | Need true parallelism |
| **Database queries** | AsyncIO | If DB supports async (asyncpg) |
| **File I/O** | Threading or AsyncIO | AsyncIO if using aiofiles |
| **API calls** | AsyncIO | Most efficient for many requests |
| **CPU + I/O mixed** | Multiprocessing + AsyncIO | Best of both |
| **Simple I/O tasks** | Threading | Easier to understand |
| **Thousands of connections** | AsyncIO | Much lighter than threads |

---

## **Basic AsyncIO Syntax**

### **Simple Example**

```python
import asyncio

async def say_hello(name):
    print(f"Hello {name}!")
    await asyncio.sleep(1)  # Non-blocking sleep
    print(f"Goodbye {name}!")

# Run single coroutine
asyncio.run(say_hello("Alice"))
```

### **Multiple Tasks**

```python
import asyncio

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)  # Yields control here
    print(f"{name} finished after {delay}s")
    return f"{name} result"

async def main():
    # Run concurrently
    results = await asyncio.gather(
        task("Task1", 2),
        task("Task2", 1),
        task("Task3", 3)
    )
    print(results)

asyncio.run(main())
```

**Output:**
```
Task1 started
Task2 started
Task3 started
Task2 finished after 1s
Task1 finished after 2s
Task3 finished after 3s
['Task1 result', 'Task2 result', 'Task3 result']
```

---

## **Real-World Example - Web Scraping**

### **Synchronous (Slow)**

```python
import requests
import time

def fetch(url):
    response = requests.get(url)
    return len(response.text)

urls = ['http://example.com'] * 10

start = time.time()
for url in urls:
    fetch(url)
print(f"Time: {time.time() - start:.2f}s")  # ~10 seconds
```

### **Threading**

```python
from concurrent.futures import ThreadPoolExecutor
import requests
import time

def fetch(url):
    response = requests.get(url)
    return len(response.text)

urls = ['http://example.com'] * 10

start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch, urls))
print(f"Time: {time.time() - start:.2f}s")  # ~2 seconds
```

### **AsyncIO (Best for this!)**

```python
import asyncio
import aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return len(await response.text())

async def main():
    urls = ['http://example.com'] * 10
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

start = time.time()
results = asyncio.run(main())
print(f"Time: {time.time() - start:.2f}s")  # ~1 second!
print(f"Total bytes: {sum(results)}")
```

---

## **AsyncIO Key Concepts**

### **1. Coroutine**
Function defined with `async def`

```python
async def my_coroutine():
    await asyncio.sleep(1)
    return "done"
```

### **2. await**
Pause execution until async operation completes

```python
async def example():
    result = await some_async_function()  # Wait here
    print(result)
```

### **3. asyncio.gather()**
Run multiple coroutines concurrently

```python
async def main():
    results = await asyncio.gather(
        coroutine1(),
        coroutine2(),
        coroutine3()
    )
```

### **4. asyncio.create_task()**
Schedule coroutine to run soon

```python
async def main():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    
    await task1
    await task2
```

### **5. Event Loop**
The core that manages and schedules async tasks

```python
# Python 3.7+
asyncio.run(main())  # Creates and manages event loop

# Older way
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

---

## **AsyncIO Patterns**

### **Pattern 1: Parallel API Calls**

```python
import asyncio
import aiohttp

async def get_user(session, user_id):
    url = f"https://api.example.com/users/{user_id}"
    async with session.get(url) as response:
        return await response.json()

async def main():
    user_ids = [1, 2, 3, 4, 5]
    
    async with aiohttp.ClientSession() as session:
        tasks = [get_user(session, uid) for uid in user_ids]
        users = await asyncio.gather(*tasks)
        
    for user in users:
        print(user)

asyncio.run(main())
```

### **Pattern 2: Producer-Consumer**

```python
import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(0.5)
        await queue.put(i)
        print(f"Produced: {i}")
    await queue.put(None)  # Sentinel

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        await asyncio.sleep(1)

async def main():
    queue = asyncio.Queue()
    
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )

asyncio.run(main())
```

### **Pattern 3: Timeout**

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(5)
    return "Done!"

async def main():
    try:
        result = await asyncio.wait_for(
            slow_operation(), 
            timeout=2.0
        )
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main())
```

### **Pattern 4: Run in Executor (Mix with Threading)**

```python
import asyncio
import time

def blocking_io():
    # Legacy blocking function
    time.sleep(2)
    return "Blocking done"

async def main():
    loop = asyncio.get_event_loop()
    
    # Run blocking code in thread pool
    result = await loop.run_in_executor(
        None,  # Default executor
        blocking_io
    )
    print(result)

asyncio.run(main())
```

---

## **AsyncIO vs Threading - Performance**

### **Memory Usage**

```python
# Threading - Each thread ~1-2MB
1000 threads = ~1-2GB memory! 😱

# AsyncIO - Tasks are lightweight
1000 tasks = ~10-50MB memory ✅
```

### **Context Switching**

```python
# Threading - OS manages switching (expensive)
Overhead per switch: ~1-10μs

# AsyncIO - Application manages (cheap)
Overhead per switch: ~0.1μs
```

### **When AsyncIO Wins**
- **Thousands of I/O operations**
- **WebSocket servers**
- **High-concurrency web apps**
- **Real-time applications**

### **When Threading Wins**
- **Legacy libraries** (no async support)
- **Simple scripts**
- **Mixed I/O and CPU work**

---

## **Common AsyncIO Libraries**

```python
# HTTP Requests
import aiohttp  # Async HTTP client

# Database
import asyncpg  # PostgreSQL
import aiomysql  # MySQL
import motor    # MongoDB

# File I/O
import aiofiles

# Redis
import aioredis

# Web Frameworks
from fastapi import FastAPI  # Built on asyncio
from aiohttp import web
```

---

## **Mixing AsyncIO with Other Methods**

### **AsyncIO + Multiprocessing (CPU + I/O)**

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

def cpu_bound(n):
    return sum(i*i for i in range(n))

async def main():
    loop = asyncio.get_event_loop()
    
    with ProcessPoolExecutor() as pool:
        # Run CPU work in processes
        result = await loop.run_in_executor(
            pool,
            cpu_bound,
            10_000_000
        )
    
    print(result)

asyncio.run(main())
```

### **AsyncIO + Threading (Legacy Code)**

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

def blocking_function():
    import time
    time.sleep(2)
    return "Done"

async def main():
    loop = asyncio.get_event_loop()
    
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            blocking_function
        )
    
    print(result)

asyncio.run(main())
```

---

## **AsyncIO Common Mistakes**

### **Mistake 1: Forgetting await**

```python
# WRONG - Returns coroutine object, doesn't run!
async def fetch():
    return "data"

async def main():
    result = fetch()  # ❌ Forgot await
    print(result)  # <coroutine object>

# CORRECT
async def main():
    result = await fetch()  # ✅
    print(result)  # "data"
```

### **Mistake 2: Blocking the Event Loop**

```python
# WRONG - Blocks entire event loop!
import time

async def bad():
    time.sleep(5)  # ❌ Blocks everything!

# CORRECT - Use async sleep
async def good():
    await asyncio.sleep(5)  # ✅ Yields control
```

### **Mistake 3: Not Using Session**

```python
# WRONG - Creates new session each time (slow!)
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

# CORRECT - Reuse session
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
```

### **Mistake 4: Mixing Sync and Async**

```python
# WRONG - Can't call async from sync directly
def sync_function():
    result = await async_function()  # ❌ SyntaxError!

# CORRECT
def sync_function():
    result = asyncio.run(async_function())  # ✅
```

---

## **Complete Comparison Table**

| Feature | Threading | Multiprocessing | AsyncIO |
|---------|-----------|-----------------|---------|
| **Concurrency Model** | Preemptive | Parallel | Cooperative |
| **GIL Impact** | ✅ Limited | ❌ None | ❌ None |
| **Memory per unit** | ~1-2MB | ~10-20MB | ~1-10KB |
| **Switching overhead** | Medium | High | Very Low |
| **Best for** | I/O-bound | CPU-bound | I/O-bound |
| **Max scalability** | ~1000s | ~100s | ~100,000s |
| **Ease of use** | Medium | Medium | Hard |
| **Debugging** | Hard | Hard | Very Hard |
| **Library support** | Excellent | Excellent | Growing |

---

## **Decision Flow Chart**

```
What kind of task?
    |
    ├─ CPU-bound (calculations, processing)
    │   └─► MULTIPROCESSING
    │
    └─ I/O-bound (network, files, database)
        |
        ├─ Simple, few operations?
        │   └─► THREADING (easier to learn)
        │
        ├─ Many concurrent operations (100+)?
        │   └─► ASYNCIO (most efficient)
        │
        ├─ Legacy libraries (no async support)?
        │   └─► THREADING
        │
        └─ Modern async libraries available?
            └─► ASYNCIO (best performance)
```

---

## **Real-World Use Cases**

### **Use Threading:**
- Desktop GUI applications
- Simple web scraping (< 100 URLs)
- Legacy codebases
- Quick prototypes

### **Use Multiprocessing:**
- Video/image processing
- Data science (pandas, numpy)
- Machine learning training
- Scientific computing

### **Use AsyncIO:**
- Web servers (FastAPI, aiohttp)
- WebSocket servers
- Chat applications
- Microservices
- Web scraping (1000+ URLs)
- Real-time data processing

---

## **Interview Questions - AsyncIO**

**Q: What is AsyncIO?**
> AsyncIO is cooperative multitasking on a single thread using async/await. Tasks voluntarily yield control during I/O operations, allowing other tasks to run.

**Q: AsyncIO vs Threading?**
> AsyncIO is single-threaded cooperative, Threading is multi-threaded preemptive. AsyncIO is more memory-efficient and can handle more concurrent operations, but requires async-compatible libraries.

**Q: When to use AsyncIO over Threading?**
> When you have many I/O-bound operations (100+), need high scalability, or are using async libraries. Threading is better for simple cases or legacy code.

**Q: What's the event loop?**
> The core scheduler that manages and executes async tasks. It decides which task runs next based on which ones are ready.

**Q: Can you mix async and sync code?**
> Yes, use `loop.run_in_executor()` to run sync code in a thread pool, or `asyncio.run()` to run async code from sync context.

**Q: What's the difference between `await` and `yield`?**
> `await` pauses async function until awaited task completes. `yield` is for generators. Both give up control but serve different purposes.

---

## **Quick AsyncIO Code Templates**

### **Template 1: Basic Async Function**
```python
import asyncio

async def my_async_function():
    await asyncio.sleep(1)
    return "result"

asyncio.run(my_async_function())
```

### **Template 2: Multiple Concurrent Tasks**
```python
async def main():
    results = await asyncio.gather(
        task1(),
        task2(),
        task3()
    )
    return results

asyncio.run(main())
```

### **Template 3: HTTP Requests**
```python
import aiohttp

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        return await asyncio.gather(*tasks)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

asyncio.run(fetch_all(urls))
```

---

## **Memory Aid**

**3 Ways to Handle I/O:**

1. **Threading** 🧵
   - "Old reliable"
   - Good for simple cases
   - ~1000 max concurrent

2. **AsyncIO** ⚡
   - "Modern and efficient"
   - Best for many operations
   - ~100,000 max concurrent

3. **Just do it sync** 🐌
   - "Sometimes simplest is best"
   - When you only have 1-5 operations

**For CPU work:** Always **Multiprocessing** ⚙️

---

## **Final Summary - All Three Methods**

```python
# THREADING - I/O-bound, simple
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(io_function, data)

# MULTIPROCESSING - CPU-bound
from concurrent.futures import ProcessPoolExecutor
with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(cpu_function, data)

# ASYNCIO - I/O-bound, many operations
import asyncio
async def main():
    results = await asyncio.gather(*[async_io(d) for d in data])
asyncio.run(main())
```

---

**Now you have the COMPLETE picture! Threading, Multiprocessing, AND AsyncIO! 🎯**

Save this, and you're ready for any Python concurrency question! 🚀