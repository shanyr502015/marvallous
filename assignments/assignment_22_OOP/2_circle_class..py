"""
Write a Python program to implement a class named Circle with the following requirements:
• The class should contain three instance variables: Radius, Area, and Circumference.
• The class should contain one class variable named PI, initialized to 3.14.
• Define a constructor (__init__) that initializes all instance variables to 0.0.
• Implement the following instance methods:
        o Accept() : accepts the radius of the circle from the user.
        o CalculateArea() : calculates the area of the circle and stores it in the Area variable.
        o CalculateCircumference() : calculates the circumference of the circle and stores it in
          the Circumference variable.
        o Display() : displays the values of Radius, Area, and Circumference.
• Create multiple objects of the Circle class and invoke all the instance methods for each object.
"""
class circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
    
    def accept(self):
        self.radius = float(input("enter radius of circle: "))
    
    def calculatearea(self):
        self.area = circle.PI * self.radius * self.radius

    def calculatecircumference(self):
        self.circumference = 2 * circle.PI * self.radius

    def display(self):
        print(f"\ncircle details:")
        print(f"radius: {self.radius}")
        print(f"area : {self.area}")
        print(f"circumference: {self.circumference}")

print("=" * 40)
circle1 = circle()
circle1.accept()
circle1.calculatearea()
circle1.calculatecircumference()
circle1.display()

print("=" * 40)
circle2 = circle()
circle2.accept()
circle2.calculatearea()
circle2.calculatecircumference()
circle2.display()

print("=" * 40)
circle3 = circle()
circle3.accept()
circle3.calculatearea()
circle3.calculatecircumference()
circle3.display()