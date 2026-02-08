# Arrays vs Lists 
    # In Python, arrays and lists are different data structures with distinct characteristics:

# LIST (built-in Python)
my_list = [1, 2, 3, "hello", 3.14, True]  # ✅ Can mix data types
# ARRAY (from 'array' module)
import array
my_array = array.array('i', [1, 2, 3, 4, 5])  # ❌ Only one data type



## 📊 Detailed Comparison Table
# -----------------------------------------------------------------------------------
# | Feature         | List                          | Array                         |
# |-----------------|-------------------------------|-------------------------------|
# | Module Required | ❌ No (built-in)              | ✅ Yes (`import array`)      |
# | Data Types      | Mixed types allowed           | Single type only              |
# | Memory Usage    | More memory                   | Less memory (efficient)       |
# | Performance     | Slower for numeric operations | Faster for numeric operations |
# | Flexibility     | Very flexible                 | Less flexible                 |
# | Common Usage    | General purpose               | Numeric/scientific computing  |
# | Syntax          | `[1, 2, 3]`                   | `array.array('i', [1, 2, 3])` |
# -----------------------------------------------------------------------------------

# 🔍 Detailed Differences
# 1️⃣ Data Type Flexibility

# LISTS - Mixed Data Types ✅
# Lists can store ANY data type together
my_list = [1, "hello", 3.14, True, [1, 2], {"key": "value"}]
print(my_list)  # Works perfectly!


# ARRAYS - Single Data Type Only ❌
import array
# Arrays must have ONE data type
my_array = array.array('i', [1, 2, 3, 4, 5])  # Only integers
# my_array = array.array('i', [1, "hello", 3.14])  # ❌ ERROR!

"""
# 2️⃣ Memory Efficiency
Memory Representation:
LIST in Memory:
┌────────┬────────┬────────┬────────┐
│Reference│Reference│Reference│Reference│  ← Stores references (pointers)
│   to    │   to    │   to    │   to    │
│  obj 1  │  obj 2  │  obj 3  │  obj 4  │
└────────┴────────┴────────┴────────┘
    ↓         ↓         ↓         ↓
  [int]   [str]    [float]  [bool]    ← Actual objects stored separately
More memory overhead!
ARRAY in Memory:
┌────┬────┬────┬────┐
│ 1  │ 2  │ 3  │ 4  │  ← Direct values stored
└────┴────┴────┴────┘ 
Less memory - more efficient!
"""
# Example:
import sys
import array
# List memory usage
my_list = [1, 2, 3, 4, 5]
print(sys.getsizeof(my_list))  # Output: ~104 bytes
# Array memory usage
my_array = array.array('i', [1, 2, 3, 4, 5])
print(sys.getsizeof(my_array))  # Output: ~80 bytes

# Arrays use less memory!
# 3️⃣ Performance Speed
# For Numeric Operations:
import array
import time
# LIST
list_nums = [1, 2, 3, 4, 5] * 100000
start = time.time()
sum(list_nums)
print(f"List time: {time.time() - start}")
# ARRAY
array_nums = array.array('i', [1, 2, 3, 4, 5] * 100000)
start = time.time()
sum(array_nums)
print(f"Array time: {time.time() - start}")
# Arrays are faster for numeric operations!

# 4️⃣ Import Requirements
# LISTS - No Import Needed
# Lists are built-in
my_list = [1, 2, 3]
# Ready to use immediately!
# ARRAYS - Import Required
# Arrays need import
import array
my_array = array.array('i', [1, 2, 3])

# 5️⃣ Type Codes (Arrays Only)

# Arrays require a type code to specify data type:
# ----------------------------------------------------------
# | Type Code | C Type        | Python Type | Size (bytes) |
# |-----------|---------------|-------------|--------------|
# | `'b'`     | signed char   | int         | 1            |
# | `'B'`     | unsigned char | int         | 1            |
# | `'i'`     | signed int    | int         | 2 or 4       |
# | `'I'`     | unsigned int  | int         | 2 or 4       |
# | `'f'`     | float         | float       | 4            |
# | `'d'`     | double        | float       | 8            |
# ----------------------------------------------------------

Examples:

import array

# Integer array
int_array = array.array('i', [1, 2, 3, 4, 5])

# Float array
float_array = array.array('f', [1.1, 2.2, 3.3])

# Double array
double_array = array.array('d', [1.11111, 2.22222])
```

---

## 💻 Practical Examples

### Example 1: Student Data

```python
# LIST - Can store mixed data
students = [
    "Alice",      # String
    20,           # Integer
    3.8,          # Float
    True          # Boolean
]
print(students)  # ✅ Works!

# ARRAY - Would need separate arrays
import array
names = ["Alice", "Bob"]  # Use list for strings
ages = array.array('i', [20, 21])
gpas = array.array('f', [3.8, 3.9])
```

### Example 2: Temperature Data

```python
import array

# ARRAY is better for numeric data
temperatures = array.array('f', [23.5, 24.1, 22.8, 25.0, 23.9])

# More memory efficient
# Faster calculations
average = sum(temperatures) / len(temperatures)
```

### Example 3: Mixed Shopping Cart

```python
# LIST is better for mixed data
shopping_cart = [
    "Laptop",           # Product name
    999.99,            # Price
    1,                 # Quantity
    True,              # In stock
    ["Intel", "16GB"]  # Specifications
]
# Can only use LIST here!
```

---

## 🎓 When to Use Each?

### Use **LISTS** when:
✅ You need to store **different data types** together  
✅ You want **maximum flexibility**  
✅ You're doing **general-purpose programming**  
✅ You need **nested structures** (lists of lists)  
✅ **Simplicity** is more important than performance  

**Example Use Cases:**
- Shopping carts
- Mixed student records
- Configuration data
- General data storage

---

### Use **ARRAYS** when:
✅ You're working with **numeric data only**  
✅ You need **memory efficiency** (large datasets)  
✅ You want **faster performance** for calculations  
✅ You're doing **scientific computing**  
✅ Interfacing with **C libraries**  

**Example Use Cases:**
- Temperature readings
- Stock prices
- Sensor data
- Image pixel values
- Audio samples

---

## 🐍 NumPy Arrays (Bonus)

For serious numeric work, use **NumPy arrays**:

```python
import numpy as np

# NumPy array - Best for scientific computing
numpy_array = np.array([1, 2, 3, 4, 5])

# Benefits:
# ✅ Very fast mathematical operations
# ✅ Broadcasting capabilities
# ✅ Multi-dimensional arrays
# ✅ Industry standard for data science

# Example: Element-wise operations
result = numpy_array * 2  # [2, 4, 6, 8, 10]
```

---

## 📝 Summary

### **Lists (Most Common)**
```python
my_list = [1, "hello", 3.14, True]
```
- 🎯 **Use for:** General purpose, mixed data
- ✅ **Pros:** Flexible, easy to use, built-in
- ❌ **Cons:** More memory, slower for math

### **Arrays (Specialized)**
```python
import array
my_array = array.array('i', [1, 2, 3, 4, 5])
```
- 🎯 **Use for:** Numeric data, memory efficiency
- ✅ **Pros:** Less memory, faster for numbers
- ❌ **Cons:** Single type only, needs import

### **NumPy Arrays (Professional)**
```python
import numpy as np
my_numpy = np.array([1, 2, 3, 4, 5])
```
- 🎯 **Use for:** Data science, machine learning
- ✅ **Pros:** Extremely fast, powerful features
- ❌ **Cons:** External library needed

---

## 🎯 Bottom Line

**For 99% of Python programming → Use LISTS** 

They're simpler, more flexible, and sufficient for most tasks!

**For numeric-heavy work → Use NumPy arrays**

They're the industry standard for data science!