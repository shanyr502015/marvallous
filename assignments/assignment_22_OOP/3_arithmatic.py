"""Write a Python program to implement a class named Arithmetic with the following
characteristics:
• The class should contain two instance variables: Value1 and Value2.
• Define a constructor (__init__) that initializes all instance variables to 0.
• Implement the following instance methods:
        o Accept() : accepts values for Value1 and Value2 from the user.
        o Addition() : returns the addition of Value1 and Value2.
        o Subtraction() : returns the subtraction of Value1 and Value2.
        o Multiplication() : returns the multiplication of Value1 and Value2.
        o Division() : returns the division of Value1 and Value2 (handle division by zero properly).
• Create multiple objects of the Arithmetic class and invoke all the instance methods."""

class arithmetic:

    def __init__(self) :
        self.value1 = 0
        self.value2 = 0

    def accept(self) :
        self.value1 = int(input("enter first number : "))
        self.value2 = int(input("enter second number : "))

    def addition(self):
        return self.value1 + self.value2
    
    def subtraction(self):
        return self.value1 - self.value2
    
    def multiplication(self):
        return self.value1 * self.value2
    
    def division (self):
        # return self.value1 / self.value2
        if self.value2 == 0:
            return "error: division by zero not allowed"
        else:
            return self.value1/self.value2
    
print("=" * 50)
obj = arithmetic()
obj.accept()
print(f"\nResults for Value1={obj.value1} and Value2={obj.value2}:")
print(f"Addition: {obj.addition()}")
print(f"Subtraction: {obj.subtraction()}")
print(f"Multiplication: {obj.multiplication()}")
print(f"Division: {obj.division()}")

print("=" * 50)
obj1 = arithmetic()
obj1.accept()
print(f"\nResults for Value1={obj1.value1} and Value2={obj1.value2}:")
print(f"Addition: {obj1.addition()}")
print(f"Subtraction: {obj1.subtraction()}")
print(f"Multiplication: {obj1.multiplication()}")
print(f"Division: {obj1.division()}")

print("=" * 50)
obj3 = arithmetic()
obj3.accept()
print(f"\nResults for Value1={obj3.value1} and Value2={obj3.value2}:")
print(f"Addition: {obj3.addition()}")
print(f"Subtraction: {obj3.subtraction()}")
print(f"Multiplication: {obj3.multiplication()}")
print(f"Division: {obj3.division()}")