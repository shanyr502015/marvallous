""" Write a Python program to implement a class named Demo with the following
specifications:
• The class should contain two instance variables: no1 and no2.
• The class should contain one class variable named Value.
• Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
• Implement two instance methods:
        o Fun() : displays the values of instance variables no1 and no2.
        o Gun() : displays the values of instance variables no1 and no2.
Create two objects of the Demo class as follows:
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)
Call the instance methods in the given sequence:
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun() """

class Demo:
    # Class variable
    Value = 0
    # Constructor to initialize instance variables
    def __init__(self, no1, no2):
        self.v1 = no1
        self.v2 = no2
    # Instance method Fun() to display instance variables
    def Fun(self):
        print(f"Fun() - no1: {self.v1}, no2: {self.v2}")
    # Instance method Gun() to display instance variablesss
    def Gun(self):
        print(f"Gun() - no1: {self.v1}, no2: {self.v2}")

# Create two objects of Demo class
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Call instance methods in the given sequence
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

# Output:
# Fun() - no1: 11, no2: 21
# Fun() - no1: 51, no2: 101
# Gun() - no1: 11, no2: 21
# Gun() - no1: 51, no2: 101