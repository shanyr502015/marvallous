# AEIP: Annual Executive Incentive Plan

class arithematic :

    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b
        print("object gets created successfully")

    def addition(self):
        ans = 0
        ans = self.no1 + self.no2
        return ans 
    
    def substraction(self):
        ans = 0
        ans = self.no1 - self.no2
        return ans 


obj1 = arithematic(11,10) # arithmatic(id(obj1),11,10) --> __init__(id(obj1),11,10) # created first object
obj2 = arithematic(21,20) # arithmatic(id(obj2),21,20) --> __init__(id(obj2),21,20) # created second object

ret = obj1.addition() # addition(id(obj1))  --> addition(1000)
print(ret) # 21

ret = obj2.substraction() # substraction(id(obj2))  --> substraction(2000)
print(ret) # 1

##################################################################################################################################################
""" 
Encapsulation in Python  Complete Explanation
What is Encapsulation?
Encapsulation is the bundling of data (characteristic/attributes) and methods (behaviour/functions) that operate on that data into a single unit (class), while restricting direct access to some components.
Real-world analogy:
Think of a TV remote 🎮:
    - Data (hidden): Internal circuits, battery voltage, IR signal codes
    - Methods (exposed): Power button, volume buttons, channel buttons
    - We don't need to know HOW it works internally, just press the buttons!
"""
class Arithmetic:
    
    def __init__(self, a, b):
        # DATA ENCAPSULATION: Bundling data inside the object
        self.no1 = a  # Data member 1
        self.no2 = b  # Data member 2
        print("Object gets created successfully")
    
    # METHOD ENCAPSULATION: Methods operate on encapsulated data
    def addition(self):
        ans = self.no1 + self.no2  # Uses internal data
        return ans 
    
    def substraction(self):
        ans = self.no1 - self.no2  # Uses internal data
        return ans 


# Creating objects with their OWN encapsulated data
obj1 = Arithmetic(11, 10)  # obj1 has its own no1=11, no2=10
obj2 = Arithmetic(21, 20)  # obj2 has its own no1=21, no2=20

# Each object maintains its own state (data)
ret = obj1.addition()      # Works on obj1's data: 11 + 10
print(ret)                 # Output: 21

ret = obj2.substraction()  # Works on obj2's data: 21 - 20
print(ret)                 # Output: 1

"""
How Encapsulation Works Here
Memory Representation:
    Memory Layout:
    --------------
    obj1 (id: 1000)
    ├── no1 = 11
    ├── no2 = 10
    └── Methods: addition(), substraction()

    obj2 (id: 2000)
    ├── no1 = 21
    ├── no2 = 20
    └── Methods: addition(), substraction()

Behind the Scenes
    obj1 = Arithmetic(11, 10)
        # Actually: Arithmetic.__init__(obj1, 11, 10)
        # Creates object at memory location (say 1000)
        # obj1.no1 = 11, obj1.no2 = 10
    obj1.addition()
        # Actually: Arithmetic.addition(obj1)
        # Python automatically passes obj1 as 'self'
        # Accesses obj1's encapsulated data
"""
# Enhanced Example with Better Encapsulation
class Arithmetic:
    
    def __init__(self, a, b):
        # PRIVATE data (better encapsulation)
        self.__no1 = a  # Private attribute
        self.__no2 = b  # Private attribute
        print(f"Object created with values: {a}, {b}")
    
    # PUBLIC interface to access private data
    def get_numbers(self):
        return self.__no1, self.__no2
    
    def set_numbers(self, a, b):
        """Controlled modification with validation"""
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.__no1 = a
            self.__no2 = b
        else:
            print("Error: Only numbers allowed!")
    
    def addition(self):
        """Encapsulated operation on private data"""
        return self.__no1 + self.__no2
    
    def subtraction(self):
        """Encapsulated operation on private data"""
        return self.__no1 - self.__no2
    
    def multiplication(self):
        return self.__no1 * self.__no2
    
    def division(self):
        if self.__no2 != 0:
            return self.__no1 / self.__no2
        return "Error: Division by zero!"


# DEMONSTRATION
print("=" * 60)
print("ENCAPSULATION DEMONSTRATION")
print("=" * 60)

# Create objects with encapsulated data
calc1 = Arithmetic(50, 10)
calc2 = Arithmetic(100, 25)

print("\n1. DATA ISOLATION (Each object has its own data):")
print(f"calc1 numbers: {calc1.get_numbers()}")
print(f"calc2 numbers: {calc2.get_numbers()}")

print("\n2. OPERATIONS ON ENCAPSULATED DATA:")
print(f"calc1 addition: {calc1.addition()}")        # 50 + 10 = 60
print(f"calc2 subtraction: {calc2.subtraction()}")  # 100 - 25 = 75

print("\n3. DATA PROTECTION (Cannot directly access private data):")
# print(calc1.__no1)  # AttributeError: 'Arithmetic' object has no attribute '__no1'

print("\n4. CONTROLLED MODIFICATION:")
calc1.set_numbers(30, 5)
print(f"After modification: {calc1.addition()}")    # 30 + 5 = 35

calc1.set_numbers("hello", 5)  # Validation prevents invalid data
print(f"After invalid attempt: {calc1.addition()}") # Still 35

print("\n5. MULTIPLE OPERATIONS ON SAME DATA:")
print(f"calc2 operations:")
print(f"  Addition: {calc2.addition()}")           # 100 + 25 = 125
print(f"  Multiplication: {calc2.multiplication()}")  # 100 * 25 = 2500
print(f"  Division: {calc2.division()}")           # 100 / 25 = 4.0

"""
## Output:
============================================================
ENCAPSULATION DEMONSTRATION
============================================================
Object created with values: 50, 10
Object created with values: 100, 25

1. DATA ISOLATION (Each object has its own data):
calc1 numbers: (50, 10)
calc2 numbers: (100, 25)

2. OPERATIONS ON ENCAPSULATED DATA:
calc1 addition: 60
calc2 subtraction: 75

3. DATA PROTECTION (Cannot directly access private data):

4. CONTROLLED MODIFICATION:
Object created with values: 30, 5
After modification: 35
Error: Only numbers allowed!
After invalid attempt: 35

5. MULTIPLE OPERATIONS ON SAME DATA:
calc2 operations:
  Addition: 125
  Multiplication: 2500
  Division: 4.0
"""
"""
Four Pillars of Encapsulation Demonstrated:
| Concept           | Explanation                    | Your Code Example                            |
|-------------------|--------------------------------|----------------------------------------------|
| Data Hiding       | Internal data is protected     | `self.__no1`, `self.__no2` are private       |
| Data Bundling     | Data + methods together        | `no1`, `no2` + `addition()`, `subtraction()` |
| Controlled Access | Access via public methods      | `get_numbers()`, `set_numbers()`             |
| Data Integrity    | Validation before modification | Check if input is numeric                    |

# Benefits You Can Mention:
1. Data Security: Private data can't be accidentally modified
   # obj1.__no1 = "invalid"  # Won't work!
   obj1.set_numbers(30, 5)    # Must use controlled interface
2. Data Isolation: Each object maintains its own state
   obj1 and obj2 have completely separate data
   Changing obj1 doesn't affect obj2
3. Flexibility: Change internal implementation without breaking external code
   # Can change how addition() works internally
   # External code using obj1.addition() remains unchanged
4. Maintainability: Easier to debug and modify

Key Interview Statement:
Encapsulation is demonstrated in my code through:
    1. Bundling data (`no1`, `no2`) and methods (`addition()`, `substraction()`) in the `Arithmetic` class
    2. Each object (obj1, obj2) maintains its own encapsulated state
    3. Methods operate on the object's own data via `self`
    4. For better encapsulation, we can make data private using double underscore and provide public getter/setter methods with validation"
"""