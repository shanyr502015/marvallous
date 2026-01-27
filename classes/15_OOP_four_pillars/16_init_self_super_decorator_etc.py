# **Python OOP Concepts - Complete Explanation** 🎯

I'll explain each concept thoroughly with examples perfect for interviews.

---

## **1. `__init__()` - Constructor Method**

### **What is `__init__()`?**

**Definition:** Special method (constructor) called automatically when an object is created.

**Purpose:** Initialize object attributes with values.

**Syntax:**
```python
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
        self.attribute = value
```

### **Complete Example:**

```python
class Student:
    def __init__(self, name, age, roll_no):
        """Constructor - called when object is created"""
        print("Constructor called!")
        self.name = name      # Instance variable
        self.age = age        # Instance variable
        self.roll_no = roll_no  # Instance variable
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll_no}")


# When object is created, __init__ is automatically called
print("=" * 60)
print("CONSTRUCTOR DEMONSTRATION")
print("=" * 60)

student1 = Student("Alice", 20, 101)  # __init__ called automatically
student2 = Student("Bob", 21, 102)    # __init__ called automatically

student1.display()
student2.display()
```

**Output:**
```
============================================================
CONSTRUCTOR DEMONSTRATION
============================================================
Constructor called!
Constructor called!
Name: Alice, Age: 20, Roll: 101
Name: Bob, Age: 21, Roll: 102
```

### **Key Points:**
- ✅ **Always named `__init__`** (double underscore on both sides)
- ✅ **Called automatically** when object is created
- ✅ **First parameter is always `self`**
- ✅ **Used to initialize attributes**
- ✅ **Cannot return any value** (except `None`)

---

## **2. `self` - Reference to Current Object**

### **What is `self`?**

**Definition:** `self` represents the **current instance** of the class. It's a reference to the object being created or used.

**Purpose:** Access attributes and methods of the current object.

### **How `self` Works - Behind the Scenes:**

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand    # self = current object
        self.model = model
    
    def display(self):
        print(f"{self.brand} {self.model}")


# What YOU write:
car1 = Car("Toyota", "Camry")
car1.display()

# What PYTHON does internally:
# Car.__init__(car1, "Toyota", "Camry")  # self = car1
# Car.display(car1)                      # self = car1
```

### **Complete Example:**

```python
print("\n" + "=" * 60)
print("UNDERSTANDING 'self'")
print("=" * 60)

class BankAccount:
    def __init__(self, account_holder, balance):
        # self refers to the current object being created
        self.account_holder = account_holder
        self.balance = balance
        print(f"Account created for {self.account_holder}")
    
    def deposit(self, amount):
        # self refers to the object that called this method
        self.balance += amount
        print(f"{self.account_holder} deposited ${amount}")
    
    def show_balance(self):
        # self allows access to object's attributes
        print(f"{self.account_holder}'s balance: ${self.balance}")


# Create multiple objects
acc1 = BankAccount("Alice", 1000)  # self = acc1 in __init__
acc2 = BankAccount("Bob", 2000)    # self = acc2 in __init__

print()
acc1.deposit(500)     # self = acc1 in deposit()
acc2.deposit(300)     # self = acc2 in deposit()

print()
acc1.show_balance()   # self = acc1
acc2.show_balance()   # self = acc2
```

**Output:**
```
============================================================
UNDERSTANDING 'self'
============================================================
Account created for Alice
Account created for Bob

Alice deposited $500
Bob deposited $300

Alice's balance: $1500
Bob's balance: $2300
```

### **Memory Visualization:**

```
Memory:
-------
acc1 (id: 1000)
├── account_holder = "Alice"
└── balance = 1500

acc2 (id: 2000)
├── account_holder = "Bob"
└── balance = 2300

When acc1.deposit(500) is called:
→ Python converts it to: BankAccount.deposit(acc1, 500)
→ Inside deposit(), 'self' = acc1
→ self.balance += amount means acc1.balance += 500
```

### **Key Points:**
- ✅ **Must be first parameter** in instance methods
- ✅ **Can be named anything** (convention is `self`)
- ✅ **Automatically passed by Python** (you don't pass it manually)
- ✅ **Refers to the current object**
- ✅ **Allows access to attributes and methods**

---

## **3. `super()` - Call Parent Class Methods**

### **What is `super()`?**

**Definition:** Built-in function to call methods from parent class.

**Purpose:** Access parent class methods/constructor, especially when overridden.

### **Complete Example:**

```python
print("\n" + "=" * 60)
print("UNDERSTANDING 'super()'")
print("=" * 60)

class Animal:
    def __init__(self, name, species):
        print(f"Animal constructor called")
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"{self.name} makes a sound")
    
    def info(self):
        print(f"Name: {self.name}, Species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent's __init__ using super()
        super().__init__(name, "Dog")
        print(f"Dog constructor called")
        self.breed = breed
    
    def make_sound(self):
        # Call parent's method first
        super().make_sound()
        # Then add child's behavior
        print(f"{self.name} says: Woof! Woof!")
    
    def dog_info(self):
        # Call parent's method
        super().info()
        print(f"Breed: {self.breed}")


# Create object
print("\nCreating Dog object:")
dog = Dog("Buddy", "Golden Retriever")

print("\nCalling make_sound():")
dog.make_sound()

print("\nCalling dog_info():")
dog.dog_info()
```

**Output:**
```
============================================================
UNDERSTANDING 'super()'
============================================================

Creating Dog object:
Animal constructor called
Dog constructor called

Calling make_sound():
Buddy makes a sound
Buddy says: Woof! Woof!

Calling dog_info():
Name: Buddy, Species: Dog
Breed: Golden Retriever
```

### **Why Use `super()`?**

**WITHOUT super():**
```python
class Parent:
    def __init__(self, x):
        self.x = x

class Child(Parent):
    def __init__(self, x, y):
        Parent.__init__(self, x)  # Direct call - not recommended
        self.y = y
```

**WITH super() (RECOMMENDED):**
```python
class Parent:
    def __init__(self, x):
        self.x = x

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)  # Cleaner, handles MRO properly
        self.y = y
```

### **Multiple Inheritance with `super()`:**

```python
print("\n" + "=" * 60)
print("super() WITH MULTIPLE INHERITANCE")
print("=" * 60)

class A:
    def __init__(self):
        print("A.__init__")
        self.a = 10

class B:
    def __init__(self):
        print("B.__init__")
        self.b = 20

class C(A, B):
    def __init__(self):
        super().__init__()  # Calls based on MRO
        print("C.__init__")
        self.c = 30

c = C()
print(f"\nMRO (Method Resolution Order): {C.__mro__}")
print(f"Attributes: a={c.a}, b={c.b if hasattr(c, 'b') else 'None'}, c={c.c}")
```

### **Key Points:**
- ✅ **Calls parent class methods**
- ✅ **Handles Method Resolution Order (MRO) automatically**
- ✅ **Syntax: `super().method_name()`**
- ✅ **Common in `__init__` to initialize parent attributes**
- ✅ **Maintains inheritance chain**

---

## **4. Decorators in Python**

### **What are Decorators?**

**Definition:** Functions that modify the behavior of other functions/methods.

**Symbol:** `@decorator_name`

### **Types of Decorators in OOP:**

#### **A. `@property` - Getter**

Makes a method accessible like an attribute.

```python
print("\n" + "=" * 60)
print("@property DECORATOR")
print("=" * 60)

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property  # Getter - read like attribute
    def radius(self):
        print("Getting radius...")
        return self._radius
    
    @property
    def area(self):
        print("Calculating area...")
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius


circle = Circle(5)

# Call like attribute, not method!
print(f"Radius: {circle.radius}")           # No () needed
print(f"Area: {circle.area}")               # No () needed
print(f"Circumference: {circle.circumference}")
```

**Output:**
```
============================================================
@property DECORATOR
============================================================
Getting radius...
Radius: 5
Calculating area...
Area: 78.53975
Circumference: 31.4159
```

---

#### **B. `@property` + `@setter` - Property with Validation**

```python
print("\n" + "=" * 60)
print("@property WITH @setter")
print("=" * 60)

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Calculated property"""
        return self._celsius * 9/5 + 32


temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

# Using setter
temp.celsius = 30  # Calls setter
print(f"Updated: {temp.celsius}°C = {temp.fahrenheit}°F")

# Validation in action
try:
    temp.celsius = -300  # Will raise error
except ValueError as e:
    print(f"Error: {e}")
```

**Output:**
```
============================================================
@property WITH @setter
============================================================
Temperature: 25°C = 77.0°F
Updated: 30°C = 86.0°F
Error: Temperature below absolute zero!
```

---

#### **C. `@staticmethod` - Method Without `self`**

**Definition:** Method that doesn't need access to instance (`self`) or class (`cls`).

```python
print("\n" + "=" * 60)
print("@staticmethod DECORATOR")
print("=" * 60)

class MathOperations:
    
    @staticmethod  # No self or cls needed
    def add(a, b):
        """Utility function - doesn't need object"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(num):
        return num % 2 == 0


# Call without creating object
print(f"Add: {MathOperations.add(5, 3)}")
print(f"Multiply: {MathOperations.multiply(4, 7)}")
print(f"Is 10 even? {MathOperations.is_even(10)}")

# Can also call with object (but not common)
math_obj = MathOperations()
print(f"Add via object: {math_obj.add(2, 8)}")
```

**Output:**
```
============================================================
@staticmethod DECORATOR
============================================================
Add: 8
Multiply: 28
Is 10 even? True
Add via object: 10
```

---

#### **D. `@classmethod` - Method With Class Reference**

**Definition:** Method that receives class (`cls`) as first parameter, not instance (`self`).

```python
print("\n" + "=" * 60)
print("@classmethod DECORATOR")
print("=" * 60)

class Employee:
    company_name = "TechCorp"  # Class variable
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    @classmethod
    def get_employee_count(cls):
        """Access class variables"""
        return cls.employee_count
    
    @classmethod
    def from_string(cls, emp_string):
        """Alternative constructor"""
        name, salary = emp_string.split('-')
        return cls(name, int(salary))
    
    @classmethod
    def change_company_name(cls, new_name):
        """Modify class variable"""
        cls.company_name = new_name


# Create employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(f"Employee count: {Employee.get_employee_count()}")
print(f"Company: {Employee.company_name}")

# Alternative constructor using classmethod
emp3 = Employee.from_string("Charlie-70000")
print(f"Employee 3: {emp3.name}, ${emp3.salary}")

# Modify class variable
Employee.change_company_name("NewTech")
print(f"New company name: {Employee.company_name}")
```

**Output:**
```
============================================================
@classmethod DECORATOR
============================================================
Employee count: 2
Company: TechCorp
Employee 3: Charlie, $70000
New company name: NewTech
```

---

#### **E. `@abstractmethod` - Abstract Method**

Already covered in abstraction section.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

### **Decorator Comparison Table:**

| Decorator | First Parameter | Access To | Use Case | Call Method |
|-----------|----------------|-----------|----------|-------------|
| **Normal method** | `self` | Instance | Instance-specific operations | `obj.method()` |
| **`@property`** | `self` | Instance | Get/Set like attribute | `obj.property` |
| **`@staticmethod`** | None | Nothing | Utility functions | `Class.method()` |
| **`@classmethod`** | `cls` | Class | Factory methods, class variables | `Class.method()` |
| **`@abstractmethod`** | `self` | Instance | Define interface | Must override |

---

## **5. Complete Real-World Example**

```python
print("\n" + "=" * 70)
print("COMPLETE OOP EXAMPLE - ALL CONCEPTS")
print("=" * 70)

from abc import ABC, abstractmethod

# ABSTRACT BASE CLASS
class BankAccount(ABC):
    """Abstract base class for bank accounts"""
    
    bank_name = "Global Bank"  # Class variable
    total_accounts = 0         # Class variable
    
    def __init__(self, account_holder, balance):
        """Constructor - initialize account"""
        print(f"Creating account for {account_holder}")
        self._account_holder = account_holder  # Protected
        self.__balance = balance               # Private
        BankAccount.total_accounts += 1
    
    @property  # Getter for account_holder
    def account_holder(self):
        return self._account_holder
    
    @property  # Getter for balance
    def balance(self):
        return self.__balance
    
    @balance.setter  # Setter with validation
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount
    
    @abstractmethod  # Must be implemented by subclasses
    def calculate_interest(self):
        pass
    
    @staticmethod  # Utility function
    def is_valid_amount(amount):
        return amount > 0
    
    @classmethod  # Class method
    def get_total_accounts(cls):
        return cls.total_accounts
    
    @classmethod  # Alternative constructor
    def from_string(cls, account_string):
        holder, balance = account_string.split('-')
        return cls(holder, float(balance))


# CONCRETE CLASS
class SavingsAccount(BankAccount):
    interest_rate = 0.05  # Class variable
    
    def __init__(self, account_holder, balance, min_balance):
        super().__init__(account_holder, balance)  # Call parent constructor
        self.min_balance = min_balance
        print(f"Savings account created with min balance: ${min_balance}")
    
    def calculate_interest(self):  # Implement abstract method
        """Calculate interest for savings account"""
        return self.balance * SavingsAccount.interest_rate
    
    def display_info(self):
        print(f"\n{'='*50}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print(f"Interest: ${self.calculate_interest():.2f}")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"{'='*50}")


# DEMONSTRATION
print("\n1. Creating accounts:")
acc1 = SavingsAccount("Alice", 10000, 1000)
acc2 = SavingsAccount("Bob", 5000, 500)

print("\n2. Using @property (getter):")
print(f"{acc1.account_holder}'s balance: ${acc1.balance}")

print("\n3. Using @staticmethod:")
print(f"Is $500 valid? {BankAccount.is_valid_amount(500)}")
print(f"Is $-100 valid? {BankAccount.is_valid_amount(-100)}")

print("\n4. Using @classmethod:")
print(f"Total accounts: {BankAccount.get_total_accounts()}")

print("\n5. Display account info:")
acc1.display_info()

print("\n6. Abstract method implementation:")
print(f"Interest earned: ${acc1.calculate_interest()}")
```

**Output:**
```
======================================================================
COMPLETE OOP EXAMPLE - ALL CONCEPTS
======================================================================

1. Creating accounts:
Creating account for Alice
Savings account created with min balance: $1000
Creating account for Bob
Savings account created with min balance: $500

2. Using @property (getter):
Alice's balance: $10000

3. Using @staticmethod:
Is $500 valid? True
Is $-100 valid? False

4. Using @classmethod:
Total accounts: 2

5. Display account info:

==================================================
Account Holder: Alice
Balance: $10000
Interest: $500.00
Bank: Global Bank
==================================================

6. Abstract method implementation:
Interest earned: $500.0
```

---

## **6. Quick Reference Summary**

### **`__init__()`**
```python
def __init__(self, parameters):
    self.attribute = value
```
- Constructor, called automatically
- Initializes object attributes

### **`self`**
```python
def method(self):
    self.attribute = value
```
- Reference to current object
- Must be first parameter

### **`super()`**
```python
super().__init__(parameters)
super().method_name()
```
- Calls parent class methods
- Handles inheritance properly

### **Decorators**
```python
@property              # Getter
@attribute.setter      # Setter
@staticmethod         # No self/cls
@classmethod          # Gets cls
@abstractmethod       # Must override
```

---

## **7. Interview Answer Template**

**Question: "Explain `__init__`, `self`, and `super()` in Python."**

**Answer:**
*"`__init__` is a special constructor method automatically called when an object is created. It initializes object attributes. `self` is a reference to the current instance of the class, allowing access to its attributes and methods - it must be the first parameter in instance methods. `super()` is used to call methods from the parent class, especially useful in inheritance to access parent's `__init__` or overridden methods. Together, these form the foundation of Python OOP."*

---

This comprehensive guide covers all essential OOP concepts in Python! 🎯