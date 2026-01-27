# **Dunder Methods / Magic Methods in Python**

I'll explain this concept comprehensively so you can confidently present it in interviews.

---

## **What are Dunder Methods?**

**Dunder = Double Underscore = `__method__`**

Also called:
- **Magic Methods**
- **Special Methods**

These are **predefined methods** in Python that allow you to define how objects of your class behave with **built-in operations** like `+`, `-`, `*`, `/`, `print()`, `len()`, etc.

### **Key Point:**
When you write `obj1 + obj2`, Python internally calls `obj1.__add__(obj2)`

---

## **Your Example Explained Step-by-Step**

### **Problem: Without Dunder Methods**

```python
class Demo:
    def __init__(self, a):
        self.no = a

obj1 = Demo(11)
obj2 = Demo(21)

print(11 + 21)      # Works: 32
print(obj1 + obj2)  # ERROR: TypeError: unsupported operand type(s) for +: 'Demo' and 'Demo'
```

**Why Error?** 
Python doesn't know how to "add" two `Demo` objects!

---

### **Solution: Using Dunder Methods**

```python
class Demo:
    def __init__(self, a):
        self.no = a
    
    # MAGIC METHOD for addition
    def __add__(self, other):
        print("Inside __add__ method")
        return self.no + other.no
    
    # MAGIC METHOD for subtraction
    def __sub__(self, other):
        return self.no - other.no
    
    # MAGIC METHOD for multiplication
    def __mul__(self, other):
        return self.no * other.no
    
    # MAGIC METHOD for division
    def __truediv__(self, other):
        return self.no / other.no


# Create objects
obj1 = Demo(11)
obj2 = Demo(21)

# Now these work!
print(11 + 21)          # 32 (normal addition)
print(obj1 + obj2)      # 32 (calls __add__(obj1, obj2))
print(obj1 - obj2)      # -10 (calls __sub__(obj1, obj2))
print(obj1 * obj2)      # 231 (calls __mul__(obj1, obj2))
print(obj1 / obj2)      # 0.523... (calls __truediv__(obj1, obj2))
```

---

## **Complete Dunder Methods Demo**

```python
class ComplexNumber:
    """Demonstrates various dunder methods"""
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    # STRING REPRESENTATION METHODS
    def __str__(self):
        """Called by print() and str() - user-friendly"""
        return f"{self.real} + {self.imag}i"
    
    def __repr__(self):
        """Called by repr() - developer-friendly, unambiguous"""
        return f"ComplexNumber({self.real}, {self.imag})"
    
    # ARITHMETIC OPERATORS
    def __add__(self, other):
        """Addition: obj1 + obj2"""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        """Subtraction: obj1 - obj2"""
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        """Multiplication: obj1 * obj2"""
        # (a+bi) * (c+di) = (ac-bd) + (ad+bc)i
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    
    # COMPARISON OPERATORS
    def __eq__(self, other):
        """Equality: obj1 == obj2"""
        return self.real == other.real and self.imag == other.imag
    
    def __ne__(self, other):
        """Not equal: obj1 != obj2"""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Less than: obj1 < obj2 (comparing magnitudes)"""
        return (self.real**2 + self.imag**2) < (other.real**2 + other.imag**2)
    
    # UNARY OPERATORS
    def __neg__(self):
        """Negation: -obj"""
        return ComplexNumber(-self.real, -self.imag)
    
    def __abs__(self):
        """Absolute value: abs(obj)"""
        return (self.real**2 + self.imag**2) ** 0.5
    
    # CONTAINER METHODS
    def __len__(self):
        """Length: len(obj) - returns magnitude as int"""
        return int(abs(self))
    
    # CALLABLE
    def __call__(self):
        """Makes object callable: obj()"""
        return f"ComplexNumber called: {self}"


# ============================================================
# DEMONSTRATION
# ============================================================
print("=" * 70)
print("DUNDER METHODS DEMONSTRATION")
print("=" * 70)

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print("\n1. STRING REPRESENTATION:")
print(f"str(c1): {str(c1)}")          # Calls __str__
print(f"repr(c1): {repr(c1)}")        # Calls __repr__
print(f"print(c1): {c1}")             # Calls __str__

print("\n2. ARITHMETIC OPERATIONS:")
print(f"c1 + c2 = {c1 + c2}")         # Calls __add__
print(f"c1 - c2 = {c1 - c2}")         # Calls __sub__
print(f"c1 * c2 = {c1 * c2}")         # Calls __mul__

print("\n3. COMPARISON OPERATIONS:")
print(f"c1 == c2: {c1 == c2}")        # Calls __eq__
print(f"c1 != c2: {c1 != c2}")        # Calls __ne__
print(f"c1 < c2: {c1 < c2}")          # Calls __lt__

print("\n4. UNARY OPERATIONS:")
print(f"-c1 = {-c1}")                 # Calls __neg__
print(f"abs(c1) = {abs(c1)}")         # Calls __abs__

print("\n5. CONTAINER OPERATIONS:")
print(f"len(c1) = {len(c1)}")         # Calls __len__

print("\n6. CALLABLE:")
print(c1())                            # Calls __call__

print("\n" + "=" * 70)
```

---

## **Output:**

```
======================================================================
DUNDER METHODS DEMONSTRATION
======================================================================

1. STRING REPRESENTATION:
str(c1): 3 + 4i
repr(c1): ComplexNumber(3, 4)
print(c1): 3 + 4i

2. ARITHMETIC OPERATIONS:
c1 + c2 = 4 + 6i
c1 - c2 = 2 + 2i
c1 * c2 = -5 + 10i

3. COMPARISON OPERATIONS:
c1 == c2: False
c1 != c2: True
c1 < c2: False

4. UNARY OPERATIONS:
-c1 = -3 + -4i
abs(c1) = 5.0

5. CONTAINER OPERATIONS:
len(c1) = 5

6. CALLABLE:
ComplexNumber called: 3 + 4i

======================================================================
```

---

## **Real-World Example: Bank Account**

```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def __str__(self):
        """User-friendly representation"""
        return f"{self.name}'s Account: ${self.balance}"
    
    def __add__(self, amount):
        """Deposit money: account + 100"""
        if isinstance(amount, (int, float)):
            self.balance += amount
            return self
        return NotImplemented
    
    def __sub__(self, amount):
        """Withdraw money: account - 50"""
        if isinstance(amount, (int, float)):
            if self.balance >= amount:
                self.balance -= amount
                return self
            else:
                print("Insufficient funds!")
                return self
        return NotImplemented
    
    def __eq__(self, other):
        """Compare balances: acc1 == acc2"""
        return self.balance == other.balance
    
    def __lt__(self, other):
        """Compare balances: acc1 < acc2"""
        return self.balance < other.balance
    
    def __len__(self):
        """Balance as integer: len(account)"""
        return int(self.balance)
    
    def __bool__(self):
        """Check if account has money: if account:"""
        return self.balance > 0


# Demonstration
print("\n" + "=" * 70)
print("REAL-WORLD EXAMPLE: BANK ACCOUNT")
print("=" * 70)

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

print(f"\nInitial accounts:")
print(acc1)
print(acc2)

print(f"\nDeposit $200 to Alice: {acc1 + 200}")
print(f"Withdraw $100 from Bob: {acc2 - 100}")

print(f"\nComparisons:")
print(f"Alice == Bob: {acc1 == acc2}")
print(f"Bob < Alice: {acc2 < acc1}")

print(f"\nBalance as length:")
print(f"len(acc1): {len(acc1)}")

print(f"\nAccount status:")
print(f"Does Alice have money? {bool(acc1)}")

empty_acc = BankAccount("Charlie", 0)
print(f"Does Charlie have money? {bool(empty_acc)}")
```

---

## **Complete List of Common Dunder Methods**

### **Category 1: Initialization & Representation**
| Method | Operator/Function | Purpose |
|--------|-------------------|---------|
| `__init__` | Constructor | Initialize object |
| `__str__` | `str()`, `print()` | User-friendly string |
| `__repr__` | `repr()` | Developer string |
| `__del__` | Destructor | Cleanup when deleted |

### **Category 2: Arithmetic Operators**
| Method | Operator | Example |
|--------|----------|---------|
| `__add__` | `+` | `obj1 + obj2` |
| `__sub__` | `-` | `obj1 - obj2` |
| `__mul__` | `*` | `obj1 * obj2` |
| `__truediv__` | `/` | `obj1 / obj2` |
| `__floordiv__` | `//` | `obj1 // obj2` |
| `__mod__` | `%` | `obj1 % obj2` |
| `__pow__` | `**` | `obj1 ** obj2` |

### **Category 3: Comparison Operators**
| Method | Operator | Example |
|--------|----------|---------|
| `__eq__` | `==` | `obj1 == obj2` |
| `__ne__` | `!=` | `obj1 != obj2` |
| `__lt__` | `<` | `obj1 < obj2` |
| `__le__` | `<=` | `obj1 <= obj2` |
| `__gt__` | `>` | `obj1 > obj2` |
| `__ge__` | `>=` | `obj1 >= obj2` |

### **Category 4: Unary Operators**
| Method | Operator | Example |
|--------|----------|---------|
| `__neg__` | `-` | `-obj` |
| `__pos__` | `+` | `+obj` |
| `__abs__` | `abs()` | `abs(obj)` |

### **Category 5: Container/Sequence Methods**
| Method | Function | Purpose |
|--------|----------|---------|
| `__len__` | `len()` | Length |
| `__getitem__` | `[]` | `obj[key]` |
| `__setitem__` | `[]=` | `obj[key] = value` |
| `__contains__` | `in` | `item in obj` |

### **Category 6: Other Useful Methods**
| Method | Function | Purpose |
|--------|----------|---------|
| `__call__` | `()` | Make object callable |
| `__bool__` | `bool()` | Truth value |
| `__hash__` | `hash()` | Hashable object |

---

## **Key Interview Points:**

### **1. What happens internally?**
```python
obj1 + obj2  
# Python translates to:
obj1.__add__(obj2)
```

### **2. Why use them?**
- Make your objects behave like built-in types
- More intuitive and Pythonic code
- Enable operator overloading (polymorphism)

### **3. Example comparison:**
```python
# Without dunder methods
result = obj1.add(obj2)  # Ugly

# With dunder methods
result = obj1 + obj2     # Clean and intuitive!
```

### **4. Important note:**
- **NOT method overloading** (same name, different parameters)
- This is **operator overloading** (giving new meaning to operators)

---

## **Interview Answer Template:**

*"Dunder methods, also called magic methods, are special methods with double underscores that allow us to define how objects of our custom classes behave with Python's built-in operations. For example, when we write `obj1 + obj2`, Python internally calls `obj1.__add__(obj2)`. By defining `__add__`, `__sub__`, `__mul__` etc., we can make our objects work seamlessly with operators like `+`, `-`, `*`, making our code more intuitive and Pythonic. This is a form of operator overloading and demonstrates polymorphism in Python."*

This explanation covers everything you need to ace interview questions about dunder methods! 🎯