""""
What is Inheritance?
    Inheritance allows a class (child) to acquire properties and methods from another class (parent), promoting code reusability and establishing IS-A relationships.
Real-world analogy:
    - Parent: Human (has eyes, nose, walks, talks)
    - Child: Student (inherits human traits + has studentID, studies)
"""
# Types of Inheritance with Your Examples

# 1. Single Inheritance: One parent → One child
# SINGLE INHERITANCE
class Parent:
    def __init__(self):
        print("Inside Parent constructor")
        self.no1 = 10
        self.no2 = 20
    
    def fun(self):
        print(f"Inside fun method of Parent: {self.no1}, {self.no2}")


class Child(Parent):  # Child inherits from Parent
    def __init__(self):
        super().__init__()  # Call parent constructor
        print("Inside Child constructor")
        self.a = 11
        self.b = 21
    
    def sun(self):
        print(f"Inside sun method of Child: {self.a}, {self.b}, {self.no1}, {self.no2}")


# Demonstration
print("=" * 60)
print("SINGLE INHERITANCE")
print("=" * 60)

cobj = Child()
print()

# Child can access its own attributes
print(f"Child's own attributes: a={cobj.a}, b={cobj.b}")

# Child can also access Parent's attributes (inherited)
print(f"Inherited from Parent: no1={cobj.no1}, no2={cobj.no2}")

# Method calls
cobj.fun()  # Parent's method
cobj.sun()  # Child's method

"""
Output:
============================================================
SINGLE INHERITANCE
============================================================
Inside Parent constructor
Inside Child constructor

Child's own attributes: a=11, b=21
Inherited from Parent: no1=10, no2=20
Inside fun method of Parent: 10, 20
Inside sun method of Child: 11, 21, 10, 20

Diagram:
    Parent
      ↓
    Child
"""

# 2. Multiple Inheritance: Multiple parents → One child
# MULTIPLE INHERITANCE
class Parent1:
    def __init__(self):
        print("Inside Parent1 constructor")
        self.x = 100
    
    def display1(self):
        print(f"Parent1 method: x={self.x}")


class Parent2:
    def __init__(self):
        print("Inside Parent2 constructor")
        self.y = 200
    
    def display2(self):
        print(f"Parent2 method: y={self.y}")


class Child(Parent1, Parent2):  # Inherits from both Parent1 and Parent2
    def __init__(self):
        Parent1.__init__(self)  # Explicitly call Parent1 constructor
        Parent2.__init__(self)  # Explicitly call Parent2 constructor
        print("Inside Child constructor")
        self.z = 300
    
    def display_all(self):
        print(f"Child has access to: x={self.x}, y={self.y}, z={self.z}")


# Demonstration
print("\n" + "=" * 60)
print("MULTIPLE INHERITANCE")
print("=" * 60)

mobj = Child()
print()

mobj.display1()    # From Parent1
mobj.display2()    # From Parent2
mobj.display_all() # Child's own method

print(f"\nMRO (Method Resolution Order): {Child.__mro__}")
"""
Output:
============================================================
MULTIPLE INHERITANCE
============================================================
Inside Parent1 constructor
Inside Parent2 constructor
Inside Child constructor

Parent1 method: x=100
Parent2 method: y=200
Child has access to: x=100, y=200, z=300

MRO (Method Resolution Order): (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>)

Diagram:
   Parent1    Parent2
       \      /
        Child
"""

# 3. Multilevel Inheritance: Parent → Child → Grandchild (chain)
# MULTILEVEL INHERITANCE
class GrandParent:
    def __init__(self):
        print("Inside GrandParent constructor")
        self.age = 70
    
    def wisdom(self):
        print(f"GrandParent's wisdom: Age {self.age}")


class Parent(GrandParent):  # Parent inherits from GrandParent
    def __init__(self):
        super().__init__()
        print("Inside Parent constructor")
        self.experience = 45
    
    def guidance(self):
        print(f"Parent's guidance: Experience {self.experience} years")


class Child(Parent):  # Child inherits from Parent (which already inherited from GrandParent)
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")
        self.energy = 100
    
    def display_all(self):
        print(f"Child has: energy={self.energy}, experience={self.experience}, age={self.age}")


# Demonstration
print("\n" + "=" * 60)
print("MULTILEVEL INHERITANCE")
print("=" * 60)

mlobj = Child()
print()

mlobj.wisdom()      # From GrandParent
mlobj.guidance()    # From Parent
mlobj.display_all() # Child's method accessing all levels

print(f"\nInheritance chain: {Child.__mro__}")

"""
Output:
============================================================
MULTILEVEL INHERITANCE
============================================================
Inside GrandParent constructor
Inside Parent constructor
Inside Child constructor

GrandParent's wisdom: Age 70
Parent's guidance: Experience 45 years
Child has: energy=100, experience=45, age=70

Inheritance chain: (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.GrandParent'>, <class 'object'>)

Diagram:
  GrandParent
      ↓
    Parent
      ↓
    Child
"""

# 4. Hierarchical Inheritance: One parent → Multiple children
# HIERARCHICAL INHERITANCE
class Parent:
    def __init__(self):
        print("Inside Parent constructor")
        self.family_name = "Smith"
    
    def common_trait(self):
        print(f"Family trait: {self.family_name}")


class Child1(Parent):  # First child
    def __init__(self):
        super().__init__()
        print("Inside Child1 constructor")
        self.skill = "Programming"
    
    def show_skill(self):
        print(f"Child1's skill: {self.skill}, Family: {self.family_name}")


class Child2(Parent):  # Second child
    def __init__(self):
        super().__init__()
        print("Inside Child2 constructor")
        self.skill = "Drawing"
    
    def show_skill(self):
        print(f"Child2's skill: {self.skill}, Family: {self.family_name}")


class Child3(Parent):  # Third child
    def __init__(self):
        super().__init__()
        print("Inside Child3 constructor")
        self.skill = "Music"
    
    def show_skill(self):
        print(f"Child3's skill: {self.skill}, Family: {self.family_name}")


# Demonstration
print("\n" + "=" * 60)
print("HIERARCHICAL INHERITANCE")
print("=" * 60)

c1 = Child1()
print()
c2 = Child2()
print()
c3 = Child3()
print()

c1.show_skill()
c2.show_skill()
c3.show_skill()

print("\nAll children share the common trait:")
c1.common_trait()
c2.common_trait()
c3.common_trait()

"""
Output:
============================================================
HIERARCHICAL INHERITANCE
============================================================
Inside Parent constructor
Inside Child1 constructor

Inside Parent constructor
Inside Child2 constructor

Inside Parent constructor
Inside Child3 constructor

Child1's skill: Programming, Family: Smith
Child2's skill: Drawing, Family: Smith
Child3's skill: Music, Family: Smith

All children share the common trait:
Family trait: Smith
Family trait: Smith
Family trait: Smith

Diagram:
```
        Parent
       /  |  \
      /   |   \
  Child1 Child2 Child3
"""


# Method Overriding Example (from your code)
# METHOD OVERRIDING (Runtime Polymorphism)
class Parent:
    def __init__(self):
        print("Inside Parent constructor")
    
    def fun(self):
        print("Inside fun method of Parent")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")
    
    def fun(self):  # Overriding parent's fun() method
        super().fun()  # Optionally call parent's version
        print("Inside fun method of Child")


# Demonstration
print("\n" + "=" * 60)
print("METHOD OVERRIDING")
print("=" * 60)

cobj = Child()
print()
cobj.fun()  # Calls Child's fun() which also calls Parent's fun()
"""
Output:
============================================================
METHOD OVERRIDING
============================================================
Inside Parent constructor
Inside Child constructor

Inside fun method of Parent
Inside fun method of Child
"""

"""
# Complete Comparison Table

| Type         | Structure                       | Example                           | Use Case                               |
|--------------|---------------------------------|-----------------------------------|----------------------------------------|
| Single       | Parent → Child                  | `Child(Parent)`                   | Basic inheritance                      |
| Multiple     | Parent1, Parent2 → Child        | `Child(Parent1, Parent2)`         | Combine features from multiple sources |
| Multilevel   | GP → Parent → Child             | `Child(Parent(GrandParent))`      | Deep hierarchies                       |
| Hierarchical | Parent → Child1, Child2, Child3 | Multiple children from one parent | Shared base functionality              |

Key Interview Points:
1. `super()` method:
    super().__init__()  # Calls parent class constructor
    super().method()    # Calls parent class method
2. Method Resolution Order (MRO):
    print(Child.__mro__)  # Shows the order Python searches for methods
3. Python doesn't support:
    - Method Overloading (same method name, different parameters)
    - But supports Method Overriding (child redefines parent's method)
4. Diamond Problem (Multiple Inheritance):
    # If both parents have same method, which one gets called?
    # Python uses C3 Linearization (MRO) to resolve this

# Real-World Examples:
# Single: Animal → Dog
# Multiple: Flyable, Swimmable → Duck
# Multilevel: Vehicle → Car → SportsCar
# Hierarchical: Employee → Manager, Developer, Designer
"""