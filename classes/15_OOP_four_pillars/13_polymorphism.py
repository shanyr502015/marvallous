# **Polymorphism in Python - Complete Guide**

I'll explain polymorphism comprehensively with examples perfect for interviews.

---

## **What is Polymorphism?**

**Polymorphism = "Many Forms"** (Greek: Poly = Many, Morph = Forms)

**Definition:** The ability of different objects to respond to the same method/function call in different ways.

**Real-world analogy:** 
- **Same action, different results**
- **"Speak" command:**
  - Dog → Barks 🐕
  - Cat → Meows 🐱
  - Cow → Moos 🐄
  - Same method name, different implementations!

---

## **Types of Polymorphism in Python**

### **1. Compile-Time Polymorphism (Method Overloading) ❌**
**NOT directly supported in Python!**

### **2. Runtime Polymorphism (Method Overriding) ✅**
**Fully supported in Python!**

### **3. Duck Typing ✅**
**Python's special feature!**

### **4. Operator Overloading (Using Dunder Methods) ✅**
**Already covered in previous topic!**

---

## **1. Method Overriding (Runtime Polymorphism)**

Same method name in parent and child classes, child class **redefines** the behavior.

```python
# RUNTIME POLYMORPHISM - METHOD OVERRIDING
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def speak(self):  # Overriding parent's speak()
        print(f"{self.name} says: Woof! Woof! 🐕")


class Cat(Animal):
    def speak(self):  # Overriding parent's speak()
        print(f"{self.name} says: Meow! Meow! 🐱")


class Cow(Animal):
    def speak(self):  # Overriding parent's speak()
        print(f"{self.name} says: Moo! Moo! 🐄")


# POLYMORPHISM IN ACTION
print("=" * 70)
print("METHOD OVERRIDING - RUNTIME POLYMORPHISM")
print("=" * 70)

# Create different objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Same method name, different behavior
print("\nCalling speak() on different objects:")
dog.speak()  # Calls Dog's version
cat.speak()  # Calls Cat's version
cow.speak()  # Calls Cow's version

# POLYMORPHIC BEHAVIOR - Same interface, different implementations
print("\n" + "=" * 70)
print("POLYMORPHIC FUNCTION")
print("=" * 70)

def make_animal_speak(animal):
    """Polymorphic function - accepts any Animal object"""
    animal.speak()  # Will call appropriate version based on object type

print("\nUsing polymorphic function:")
animals = [dog, cat, cow]
for animal in animals:
    make_animal_speak(animal)
```

**Output:**
```
======================================================================
METHOD OVERRIDING - RUNTIME POLYMORPHISM
======================================================================

Calling speak() on different objects:
Buddy says: Woof! Woof! 🐕
Whiskers says: Meow! Meow! 🐱
Bessie says: Moo! Moo! 🐄

======================================================================
POLYMORPHIC FUNCTION
======================================================================

Using polymorphic function:
Buddy says: Woof! Woof! 🐕
Whiskers says: Meow! Meow! 🐱
Bessie says: Moo! Moo! 🐄
```

---

## **2. Duck Typing (Python's Special Feature)**

**"If it walks like a duck and quacks like a duck, it must be a duck!"**

Python doesn't care about the **type** of object, only about what **methods** it has.

```python
# DUCK TYPING - Python's Dynamic Polymorphism
print("\n" + "=" * 70)
print("DUCK TYPING")
print("=" * 70)

class Bird:
    def fly(self):
        print("Bird is flying 🐦")


class Airplane:
    def fly(self):
        print("Airplane is flying ✈️")


class Superman:
    def fly(self):
        print("Superman is flying 🦸")


# POLYMORPHIC FUNCTION - No inheritance required!
def make_it_fly(flying_object):
    """Accepts ANY object that has a fly() method"""
    flying_object.fly()


# Different types, same interface
bird = Bird()
plane = Airplane()
hero = Superman()

print("\nDuck Typing in action:")
make_it_fly(bird)   # Works!
make_it_fly(plane)  # Works!
make_it_fly(hero)   # Works!

# No inheritance relationship, but still polymorphic!
print("\nNote: These classes have NO common parent!")
```

**Output:**
```
======================================================================
DUCK TYPING
======================================================================

Duck Typing in action:
Bird is flying 🐦
Airplane is flying ✈️
Superman is flying 🦸

Note: These classes have NO common parent!
```

---

## **3. Operator Overloading (Dunder Methods)**

Already covered, but here's a quick recap:

```python
# OPERATOR OVERLOADING
print("\n" + "=" * 70)
print("OPERATOR OVERLOADING")
print("=" * 70)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Polymorphic + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(f"\nv1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")  # Same + operator, different behavior

print("\nSame operator works with different types:")
print(f"5 + 3 = {5 + 3}")              # Integer addition
print(f"'Hello' + 'World' = {'Hello' + 'World'}")  # String concatenation
print(f"[1,2] + [3,4] = {[1,2] + [3,4]}")  # List concatenation
```

---

## **Real-World Example: Payment Processing System**

```python
# REAL-WORLD POLYMORPHISM EXAMPLE
print("\n" + "=" * 70)
print("REAL-WORLD EXAMPLE: PAYMENT SYSTEM")
print("=" * 70)

class Payment:
    """Base class for all payment methods"""
    def __init__(self, amount):
        self.amount = amount
    
    def process_payment(self):
        """To be overridden by child classes"""
        pass


class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    
    def process_payment(self):
        print(f"Processing Credit Card payment of ${self.amount}")
        print(f"Card: ****{self.card_number[-4:]}")
        print("Payment approved via Credit Card ✓")


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def process_payment(self):
        print(f"Processing PayPal payment of ${self.amount}")
        print(f"Account: {self.email}")
        print("Payment approved via PayPal ✓")


class CryptoPayment(Payment):
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.wallet_address = wallet_address
    
    def process_payment(self):
        print(f"Processing Cryptocurrency payment of ${self.amount}")
        print(f"Wallet: {self.wallet_address[:10]}...")
        print("Payment approved via Crypto ✓")


# POLYMORPHIC PAYMENT PROCESSOR
def execute_payment(payment_method):
    """Accepts any Payment object - polymorphic function"""
    print("\n" + "-" * 50)
    payment_method.process_payment()
    print("-" * 50)


# Create different payment methods
payments = [
    CreditCardPayment(100, "1234567890123456"),
    PayPalPayment(250, "user@example.com"),
    CryptoPayment(500, "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb")
]

print("\nProcessing different payment methods:")
for payment in payments:
    execute_payment(payment)  # Same function, different implementations!
```

**Output:**
```
======================================================================
REAL-WORLD EXAMPLE: PAYMENT SYSTEM
======================================================================

Processing different payment methods:

--------------------------------------------------
Processing Credit Card payment of $100
Card: ****3456
Payment approved via Credit Card ✓
--------------------------------------------------

--------------------------------------------------
Processing PayPal payment of $250
Account: user@example.com
Payment approved via PayPal ✓
--------------------------------------------------

--------------------------------------------------
Processing Cryptocurrency payment of $500
Wallet: 0x742d35Cc...
Payment approved via Crypto ✓
--------------------------------------------------
```

---

## **Another Example: Shape Calculator**

```python
# SHAPE CALCULATOR - POLYMORPHISM
print("\n" + "=" * 70)
print("SHAPE CALCULATOR")
print("=" * 70)

import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c


# POLYMORPHIC FUNCTION
def print_shape_info(shape, name):
    """Works with any Shape object"""
    print(f"\n{name}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")


# Create different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

print("\nCalculating properties of different shapes:")
print_shape_info(circle, "Circle (radius=5)")
print_shape_info(rectangle, "Rectangle (4x6)")
print_shape_info(triangle, "Triangle (3,4,5)")
```

---

## **Method Overloading Workaround in Python**

Python doesn't support traditional method overloading, but we can simulate it:

```python
# METHOD OVERLOADING WORKAROUND
print("\n" + "=" * 70)
print("METHOD OVERLOADING WORKAROUND")
print("=" * 70)

class Calculator:
    def add(self, *args):
        """Accepts variable number of arguments"""
        return sum(args)
    
    def multiply(self, *args, **kwargs):
        """With default values"""
        result = 1
        for num in args:
            result *= num
        
        # Optional multiplier
        if 'multiplier' in kwargs:
            result *= kwargs['multiplier']
        
        return result


calc = Calculator()

print("\nFlexible method calls:")
print(f"add(5, 10) = {calc.add(5, 10)}")
print(f"add(5, 10, 15) = {calc.add(5, 10, 15)}")
print(f"add(1, 2, 3, 4, 5) = {calc.add(1, 2, 3, 4, 5)}")

print(f"\nmultiply(2, 3) = {calc.multiply(2, 3)}")
print(f"multiply(2, 3, 4) = {calc.multiply(2, 3, 4)}")
print(f"multiply(2, 3, multiplier=10) = {calc.multiply(2, 3, multiplier=10)}")
```

---

## **Comparison Table**

| Feature | Method Overriding | Duck Typing | Operator Overloading |
|---------|------------------|-------------|---------------------|
| **Inheritance Required?** | Yes | No | No |
| **Runtime/Compile** | Runtime | Runtime | Runtime |
| **Example** | `speak()` in Animal classes | `fly()` in different classes | `+` operator |
| **Python Support** | ✅ Full | ✅ Full | ✅ Full |

---

## **Key Interview Points**

### **1. Definition:**
*"Polymorphism allows objects of different classes to be treated through the same interface, with each object responding in its own way."*

### **2. Benefits:**
- **Code Reusability**: Write once, use with many types
- **Flexibility**: Easy to add new types without changing existing code
- **Maintainability**: Cleaner, more organized code

### **3. Python's Unique Feature:**
*"Python uses **Duck Typing**, which is more flexible than traditional polymorphism. We don't need inheritance - if an object has the required method, it works!"*

### **4. Real-world Use Cases:**
- Payment processing systems
- Database connectors (MySQL, PostgreSQL, MongoDB - same interface)
- File handlers (CSV, JSON, XML - same read/write methods)
- Shape calculators
- Vehicle management systems

### **5. Method Overloading:**
*"Python doesn't support traditional method overloading (same name, different parameters), but we can achieve similar functionality using default arguments, `*args`, and `**kwargs`."*

---

## **Complete Interview Answer Template**

*"Polymorphism in Python means 'many forms' - the ability of different objects to respond to the same method call in different ways. Python supports runtime polymorphism through **method overriding**, where child classes redefine parent class methods. Python also has **duck typing**, where we don't need inheritance - if an object has the required method, it works. Additionally, we have **operator overloading** using dunder methods like `__add__`, `__sub__`, etc. Python doesn't support compile-time method overloading, but we can achieve similar results using `*args` and `**kwargs`. Polymorphism makes code more flexible, reusable, and maintainable."*

This comprehensive guide covers everything you need to explain polymorphism confidently in interviews! 🎯