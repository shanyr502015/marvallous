''' Core Concept: Everything is an Object in Python: Means that every single value in Python - integers, strings, functions, classes, modules everything is an instance of some class with:
    1. An identity (memory address)
    2. A type (its class)
    3. Attributes & methods (data & behavior)
This is different from languages like C or Java where primitives (int, char, etc.) are just raw values in memory without any associated behavior. '''
#---------------------------------------------------------------------------------------------------------------
# Example 1: Even integers are full-fledged objects
x = 42 # It's an instance of the int class
print(type(x))  # <class 'int'>
print(id(x))  # # It has an identity (memory location)

# It has methods you can call
print(x.bit_length())  # 6 (number of bits needed to represent 42)
print(x.to_bytes(2, 'big'))  # b'\x00*' (convert to bytes)

# Even the type itself is an object!
print(type(int))  # <class 'type'>
print(id(int))  # Has its own memory address
# Why this matters: In languages like C, `42` is just bits in memory. In Python, it's an object with capabilities.

#---------------------------------------------------------------------------------------------------------------
# Example 2: Functions are objects too: This is where it gets wild and powerful:
def greet(name):
    return f"Hello, {name}!"

# The function is an object
print(type(greet))  # <class 'function'>
print(id(greet))  # Has a memory address
# Functions have attributes
print(greet.__name__)  # 'greet'
greet.custom_property = "I added this!"
print(greet.custom_property)  # 'I added this!'

# You can pass functions around like any other object
def execute_function(func, arg):
    return func(arg)

result = execute_function(greet, "World")  # "Hello, World!"
# You can store functions in data structures

function_list = [greet, print, len]
function_list[0]("Alice")  # Calls greet("Alice")

# NOTE: This is why Python has first-class functions - they're objects like anything else.

#---------------------------------------------------------------------------------------------------------------
# Example 3: Classes are objects (this blows minds)
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name):
        self.name = name

# The class itself is an object!
print(type(Dog))  # <class 'type'>
print(Dog.__name__)  # 'Dog'
print(Dog.species)  # 'Canis familiaris'

# You can assign classes to variables
AnimalType = Dog
my_pet = AnimalType("Buddy")  # Creates a Dog instance

# You can dynamically create classes at runtime
def create_class(class_name):
    return type(class_name, (), {"greeting": "Hello"})

DynamicClass = create_class("MyClass")
instance = DynamicClass()
print(instance.greeting)  # 'Hello'

#---------------------------------------------------------------------------------------------------------------
# Example 4: Even modules are objects

import math

print(type(math))  # <class 'module'>
print(dir(math))  # Lists all attributes
print(math.__name__)  # 'math'

# You can pass modules around
def use_module(module):
    return module.pi

print(use_module(math))  # 3.141592653589793
#---------------------------------------------------------------------------------------------------------------

""" 
The Memory Hook (Remember This Forever) : Here's your eternal mnemonic: In Python, there are no primitives - only participants.
Everything participates in object system. 
Everything can:
- Be assigned to variables
- Be passed as arguments  
- Be returned from functions
- Have attributes attached
- Be introspected with `type()`, `id()`, `dir()` 
"""
#---------------------------------------------------------------------------------------------------------------
# Example 5: Practical Implications
""" 
This is why Python is so flexible and why things like decorators, metaclasses, and introspection work:
Because functions are objects, decorators work 
"""
def my_decorator(func):
    func.decorated = True
    return func

@my_decorator
def my_function():
    pass

print(my_function.decorated)  # True

# Because everything has __class__, you can introspect anything
print((42).__class__)  # <class 'int'>
print(greet.__class__)  # <class 'function'>
#---------------------------------------------------------------------------------------------------------------

# One Final Mind-Bender:  Everything is an object, including 'object' itself
print(type(object))  # <class 'type'>
# And 'type' is an object too
print(type(type))  # <class 'type'> # type is an instance of itself!

"""
# Bottom line: Python doesn't distinguish between "data" and "objects.
# There's no special category for primitives. 
# Everything in Python inherits from `object`, has a type, and can be manipulated uniformly. 
# That's the power and the elegance.
"""