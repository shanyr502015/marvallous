# Array Data Structures 
"""
Why Do We Need Arrays?
The Problem --> Imagine you need to store the ages of 10 students:
Without Arrays (Bad Approach):
    student1_age = 18
    student2_age = 19
    student3_age = 20
    student4_age = 21
    student5_age = 19
    student6_age = 20
    student7_age = 18
    student8_age = 22
    student9_age = 19
    student10_age = 21
Issues with this approach:
- ❌ Too many variables to create
- ❌ Difficult to manipulate
- ❌ Hard to keep track of
- ❌ What if there are 20, 50, or 100 students?
"""

# The Solution: Arrays (Lists in Python)
ages = [18, 19, 20, 21, 19, 20, 18, 22, 19, 21] # One variable holds all values!

# What is an Array? --> An array is special variable that can hold more than one value at time.
# Key Characteristics:
    # 1. Contiguous Memory Storage - Elements are stored in sequential memory locations
    # 2. Index-Based Access - Elements can be accessed using their index
    # 3. Same Data Type - Typically stores elements of the same type

# Arrays in Python
    # Important Note: Python doesn't have built-in array support like other languages (C, Java).
    # Instead, Python uses LISTS to achieve the same functionality.

# Creating a list (Python's array equivalent)
ages = [18, 19, 20, 21, 19, 20, 18, 22, 19, 21]

# 📊 Memory Representationm: Here's how the array is stored in memory:
# Memory Address:  1000   1004   1008   1012   1016   1020   1024   1028   1032   1036
#                   ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓
# Array Elements:  [18]   [19]   [20]   [21]   [19]   [20]   [18]   [22]   [19]   [21]
#                   ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓
# Index:            0      1      2      3      4      5      6      7      8      9
# Key Point: Elements are stored in contiguous (sequential) memory locations.

# 🔢 Indexing in Arrays
# CRITICAL RULE: Array indexing starts from 0, NOT 1
# Array:  [18, 19, 20, 21, 19, 20, 18, 22, 19, 21]
# Index:    0   1   2   3   4   5   6   7   8   9

# Accessing Elements:
ages = [18, 19, 20, 21, 19, 20, 18, 22, 19, 21]
# Access first student's age (index 0)
first_age = ages[0]  # Returns 18
# Access fifth student's age (index 4)
fifth_age = ages[4]  # Returns 19
# Access tenth student's age (index 9)
tenth_age = ages[9]  # Returns 21

# General Formula:
    # - To access the nth element: Use index `n - 1`
    # - Array of length n: Has indices from `0` to `n - 1`
            # | Element Position    | Index |
            # |---------------------|-------|
            # | 1st element | 0     |
            # | 2nd element | 1     |
            # | 3rd element | 2     |
            # | 5th element | 4     |
            # | nth element | n - 1 |
            # | Last element (n=10) | 9     |

# 🏢 Real-World Analogy: Apartment Building
# Think of an array like an apartment building:
    # Apartment Building (Array)
    # ┌─────────────────────────┐
    # │  House[0] - First House │  ← Index 0
    # ├─────────────────────────┤
    # │  House[1] - Second House│  ← Index 1
    # ├─────────────────────────┤
    # │  House[2] - Third House │  ← Index 2
    # └─────────────────────────┘
# - House = Individual Element
# - Apartment = Array (collection of houses)
# - House Number = Index (starting from 0)

apartment = ["House A", "House B", "House C"]
#            Index 0     Index 1    Index 2

# 💡 Quick Examples
# Create an array (list)
scores = [85, 90, 78, 92, 88]
# Access elements
print(scores[0])    # Output: 85 (first element)
print(scores[2])    # Output: 78 (third element)
print(scores[4])    # Output: 88 (fifth element)
# Length of array
print(len(scores))  # Output: 5
# Last element (using length)
print(scores[len(scores) - 1])  # Output: 88

# 📝 Key Takeaways
    # 1. Arrays solve the problem of managing multiple related values
    # 2. One variable can store multiple values
    # 3. Indexing starts at 0, not 1
    # 4. Elements are stored in contiguous memory
    # 5. Python uses lists instead of traditional arrays
    # 6. Access pattern: nth element = index (n-1)
    # 7. Array of length n has indices: 0 to n-1

# ⚡ Why This Matters
    # Arrays are fundamental because they:
        # - Make code cleaner and more manageable
        # - Enable efficient data manipulation
        # - Allow easy iteration through elements
        # - Provide constant-time access to elements (O(1))